# -*- coding: utf-8 -*-
"""
Pelican Comment System
======================

A Pelican plugin, which allows you to add static comments to your articles.

Author: Bernhard Scheirle
"""
from __future__ import unicode_literals
import logging
import os
import copy
from itertools import chain

from pelican import signals
from pelican.readers import Readers
from pelican.writers import Writer

from . comment import Comment
from . import avatars

__version__ = "1.4.0"

PCS_KEY = 'PELICAN_COMMENT_SYSTEM'
PCS_META_KEY = 'pcs'

logger = logging.getLogger(__name__)

_all_comments = []
_pelican_writer = None
_pelican_obj = None


def deep_set_default(root_dict, root_key, default_dict):
    '''
    :type root_dict: dict(mixed, mixed)
    :type root_key: mixed
    :type default_dict: dict(mixed, mixed)

    root_dict.setdefault(root_key, default_dict),
    but also considers child dicts.
    '''
    root_dict.setdefault(root_key, default_dict)
    for key, value in default_dict.items():
        if key not in root_dict[root_key]:
            root_dict[root_key][key] = value
        elif isinstance(value, dict):
            deep_set_default(root_dict[root_key], key, value)


def on_initialized(pelican):
    '''
    :type pelican: Pelican

    Executed after the main pelican object initialized
    (After plugin registration).

    Sets the default configuration for this plugin.
    '''
    from pelican.settings import DEFAULT_CONFIG

    default_pcs_config = {
        'DIR': 'comments',
        'IDENTICON': {
            'OUTPUT_PATH': 'images/identicon',
            'DATA': (),
            'SIZE': 72,
        },
        'AUTHORS':  {},
        'FEED':     os.path.join('feeds', 'comment.%s.atom.xml'),
        'FEED_ALL': os.path.join('feeds', 'comments.all.atom.xml'),
        'DEFAULT_STATE': {
            'Article': 'open',  # closed, hidden
            'Page':    'open',
            'Draft':   'closed',
        }
    }

    default_root_config = [
        ('COMMENT_URL', '#comment-{slug}')
    ]

    # set default pcs config; merge with user specified config if necessary
    deep_set_default(DEFAULT_CONFIG,   PCS_KEY, default_pcs_config)
    deep_set_default(pelican.settings, PCS_KEY, default_pcs_config)

    # set default root config
    for key, value in default_root_config:
        DEFAULT_CONFIG.setdefault(key, value)
        pelican.settings.setdefault(key, value)

    # exclude comment dir from pages and articles
    exclude_default = DEFAULT_CONFIG[PCS_KEY]['DIR']
    exclude_pelican = pelican.settings[PCS_KEY]['DIR']

    DEFAULT_CONFIG.setdefault('PAGE_EXCLUDES',      []).append(exclude_default)
    DEFAULT_CONFIG.setdefault('ARTICLE_EXCLUDES',   []).append(exclude_default)
    pelican.settings.setdefault('PAGE_EXCLUDES',    []).append(exclude_pelican)
    pelican.settings.setdefault('ARTICLE_EXCLUDES', []).append(exclude_pelican)

    global _pelican_obj
    _pelican_obj = pelican


def on_article_generator_init(article_generator):
    '''
    :type article_generator: ArticlesGenerator

    Executed in ArticlesGenerator::__init__

    Initializes the avatars submodule and resets the plugin state in
    autoreload mode.
    '''
    avatars.init(
        article_generator.settings['OUTPUT_PATH'],
        article_generator.settings[PCS_KEY]['IDENTICON']['OUTPUT_PATH'],
        article_generator.settings[PCS_KEY]['IDENTICON']['DATA'],
        article_generator.settings[PCS_KEY]['IDENTICON']['SIZE'] / 3,
        article_generator.settings[PCS_KEY]['AUTHORS'],
    )

    # Reset old states (autoreload mode)
    global _all_comments
    global _pelican_writer
    _pelican_writer = _pelican_obj.get_writer()
    _all_comments = []


def on_article_generator_finalized(article_generator):
    '''
    :type article_generator: ArticlesGenerator

    Executed at the end of ArticlesGenerator::generate_context
    '''
    for article in article_generator.articles:
        process_comments(article_generator, article)


def on_page_generator_finalized(page_generator):
    '''
    :type page_generator: PagesGenerator

    Executed at the end of PagesGenerator::generate_context
    '''
    for page in page_generator.pages:
        process_comments(page_generator, page)


def write_feed(gen, items, context, slug):
    '''
    :type gen: Generator
    :type items: list[Comment]
    :type context: dict(str, mixed)
    :type slug: str

    Generates a comment feed with the given items and for the article with
    the slug: slug.
    '''
    if gen.settings[PCS_KEY]['FEED'] is None:
        return

    path = gen.settings[PCS_KEY]['FEED'] % slug
    _pelican_writer.write_feed(items, context, path)


def warn_on_slug_collision(items):
    '''
    :type items: list[Comment]

    Logs a warning if there are multiple comments with the same slug.
    '''
    slugs = {}
    for comment in items:
        if comment.slug not in slugs:
            slugs[comment.slug] = [comment]
        else:
            slugs[comment.slug].append(comment)

    for slug, itemList in slugs.items():
        len_ = len(itemList)
        if len_ > 1:
            logger.warning('There are %s comments with the same slug: %s',
                           len_, slug)
            for x in itemList:
                logger.warning('    %s', x.source_path)


def mirror_to_translations(content):
    '''
    :type content: Content

    Copies the comments stats of the given content to its translations.
    '''
    for translation in content.translations:
        translation.comments_count = content.comments_count
        translation.comments = content.comments


def process_comments(gen, content):
    '''
    :type gen: Generator
    :type content: Content

    Processes all comments for the given content object.
    '''
    global _all_comments

    content.comments_count = 0
    content.comments = []
    mirror_to_translations(content)

    # Modify the local context, so we get proper values for the feed
    context = copy.copy(gen.context)
    context['SITEURL'] += "/" + content.url
    context['SITENAME'] += " - Comments: " + content.title
    context['SITESUBTITLE'] = ""
    context[PCS_KEY + '__FORCE_SANE_DATE'] = content.date

    # Load default state if not set by content
    if not hasattr(content.metadata, PCS_META_KEY):
        content_type = content.__class__.__name__
        default_state_dict = context[PCS_KEY]['DEFAULT_STATE']
        if hasattr(default_state_dict, content_type):
            content.metadata[PCS_META_KEY] = default_state_dict[content_type]
        else:
            content.metadata[PCS_META_KEY] = 'open'

    state = content.metadata[PCS_META_KEY].lower()
    if state is 'open':
        # Normal operation.
        pass
    elif state is 'closed':
        # This state must be handled by the theme.
        # Normal operation.
        pass
    elif state is 'hidden':
        # This state must also be handled by the theme.
        logger.debug("Comments are hidden for: %s", content.slug)
        write_feed(gen, [], context, content.slug)
        return
    else:
        assert(False, "Unknown state: %s" % state)

    comment_folder = os.path.join(
        gen.settings['PATH'],
        gen.settings[PCS_KEY]['DIR'],
        content.slug
    )

    if not os.path.isdir(comment_folder):
        logger.debug("No comments found for: %s", content.slug)
        write_feed(gen, [], context, content.slug)
        return

    reader = Readers(gen.settings)
    comments = []
    replies = []

    for file in os.listdir(comment_folder):
        name, extension = os.path.splitext(file)
        if extension[1:].lower() in reader.extensions:
            comment = reader.read_file(
                base_path=comment_folder, path=file,
                content_class=Comment, context=context)

            comment.article = content
            _all_comments.append(comment)

            if hasattr(comment, 'replyto'):
                replies.append(comment)
            else:
                comments.append(comment)

    feed_items = sorted(comments + replies)
    feed_items.reverse()
    warn_on_slug_collision(feed_items)

    write_feed(gen, feed_items, context, content.slug)

    # TODO: Fix this O(n²) loop
    for reply in replies:
        found_parent = False
        for comment in chain(comments, replies):
            if comment.slug == reply.replyto:
                comment.addReply(reply)
                found_parent = True
                break
        if not found_parent:
            logger.warning('Comment "%s/%s" is a reply to non-existent '
                           'comment "%s". Make sure the replyto attribute is '
                           'set correctly.',
                           content.slug, reply.slug, reply.replyto)

    count = 0
    for comment in comments:
        comment.sortReplies()
        count += comment.countReplies()

    comments = sorted(comments)

    content.comments_count = len(comments) + count
    content.comments = comments
    mirror_to_translations(content)


def on_feed_generated(context, feed):
    '''
    :type context: dict(str, mixed)
    :type feed: SyndicationFeed

    Executed after a feed gets generated but befor it gets written to disk.

    If the feed is a pcs feed and is empty set the date to a fixed date.
    '''
    force_date = context.get(PCS_KEY + '__FORCE_SANE_DATE', None)
    if force_date is None:
        return

    if feed.num_items() <= 0:
        # Monkey patch the feed to return a static date
        # Fixes: https://github.com/getpelican/pelican-plugins/issues/780
        feed.__dict__['latest_post_date'] = lambda: force_date


def on_finalized(pelican):
    '''
    Executed just before pelican exits.

    Generates the avatars and writes the pcs all comment feed.
    Prints the number of processed comments.
    '''
    avatars.generateAndSaveMissingAvatars()

    # Write FEED_ALL
    if pelican.settings[PCS_KEY]['FEED_ALL'] is None:
        return

    context = copy.copy(pelican.settings)
    context['SITENAME'] += " - All Comments"
    context['SITESUBTITLE'] = ""
    path = context[PCS_KEY]['FEED_ALL']

    global _all_comments
    _all_comments = sorted(_all_comments)
    _all_comments.reverse()

    for com in _all_comments:
        com.title = com.article.title + " - " + com.title
        com.override_url = com.article.url + com.url

    _pelican_writer.write_feed(_all_comments, context, path)

    print('Processed %s comment(s)' % len(_all_comments))


def register():
    '''Register the plugin only if required signals are available'''

    signal_handlers_db = [
        # (signal name,       optional signal, signal handler)
        ('initialized',                 False, on_initialized),
        ('article_generator_init',      False, on_article_generator_init),
        ('article_generator_finalized', False, on_article_generator_finalized),
        ('page_generator_finalized',    False, on_page_generator_finalized),
        ('feed_generated',              True,  on_feed_generated),
        ('finalized',                   False, on_finalized)
    ]

    # check that all required signals are available
    for name, optional, _ in signal_handlers_db:
        if not hasattr(signals, name) and not optional:
            logger.error(
                'The pelican_comment_system plugin requires Pelican 3.4.0 '
                'or later.')
            logger.debug(('Missing Signal: {}').format(name))
            return

    # register all available signals (optionals may not be available)
    for name, _, handler in signal_handlers_db:
        if not hasattr(signals, name):
            continue

        sig = getattr(signals, name)
        sig.connect(handler)
