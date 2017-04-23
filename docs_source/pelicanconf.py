# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from md_tabs import TabExtension

SITEURL = "https://scheirle.github.io/pelican_comment_system"
SITENAME = "Pelican Comment System"
TIMEZONE = 'Europe/Berlin'
LOCALE = 'en_US.UTF-8'
DEFAULT_LANG = 'en'

# Paths
PATH = 'content'
ARTICLE_PATHS = ['articles']
PAGE_PATHS = ['pages']

# URLs
RELATIVE_URLS = True
# URL
BASE_ARTICLE_URL        = 'posts/'
BASE_ARTICLE_URL_YEAR   = BASE_ARTICLE_URL + '{date:%Y}/'
BASE_ARTICLE_URL_MONTH  = BASE_ARTICLE_URL_YEAR + '{date:%B}/'
BASE_ARTICLE_URL_DAY    = BASE_ARTICLE_URL_MONTH + '{date:%d}/'

ARTICLE_URL             = BASE_ARTICLE_URL_DAY + '{slug}/'
ARTICLE_SAVE_AS         = ARTICLE_URL + 'index.html'
#ARTICLE_LANG_URL       = ARTICLE_URL + '{lang}/'
#ARTICLE_LANG_SAVE_AS   = ARTICLE_LANG_URL + 'index.html'

PAGE_URL                = 'pages/{slug}/'
PAGE_SAVE_AS            = PAGE_URL + 'index.html'
#PAGE_LANG_URL          = PAGE_URL + '{lang}/'
#PAGE_LANG_SAVE_AS      = PAGE_LANG_URL + 'index.html'

CATEGORY_URL            = 'category/{slug}/'
CATEGORY_SAVE_AS        = CATEGORY_URL + 'index.html'
CATEGORIES_URL          = 'categories/'
CATEGORIES_SAVE_AS      = 'categories/index.html'

TAG_URL     = 'tag/{slug}/'
TAG_SAVE_AS = TAG_URL + 'index.html'

TAGS_URL     = 'tags/'
TAGS_SAVE_AS = TAGS_URL + 'index.html'

AUTHOR_URL      = 'author/{slug}/'
AUTHOR_SAVE_AS  = AUTHOR_URL + 'index.html'

AUTHORS_URL     = 'authors/'
AUTHORS_SAVE_AS = AUTHORS_URL + 'index.html'

ARCHIVES_URL            = BASE_ARTICLE_URL
ARCHIVES_SAVE_AS        = BASE_ARTICLE_URL       + 'index.html'
YEAR_ARCHIVE_SAVE_AS    = BASE_ARTICLE_URL_YEAR  + 'index.html'
MONTH_ARCHIVE_SAVE_AS   = BASE_ARTICLE_URL_MONTH + 'index.html'
DAY_ARCHIVE_SAVE_AS     = BASE_ARTICLE_URL_DAY   + 'index.html'

DEFAULT_PAGINATION = 6
DEFAULT_ORPHANS = 2  # The minimum number of articles allowed on the last page.
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

# Feeds
AUTHOR_FEED_RSS = None
AUTHOR_FEED_ATOM = None
CATEGORY_FEED_RSS = None
CATEGORY_FEED_ATOM = None
FEED_ALL_RSS = None
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ATOM = None
FEED_RSS = None
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None

# Theme
THEME = 'theme'
# DIRECT_TEMPLATES = []
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (
    ('Home', SITEURL),
    ('Blog/News', SITEURL + '/category/blog/'),
    ('GitHub', 'https://github.com/Scheirle/pelican_comment_system'),
)

# Plugins
PLUGIN_PATHS = ['../']
PLUGINS = ['pelican_comment_system']

# Markdown
MARKDOWN = {
    'extensions': ['markdown.extensions.extra', TabExtension()],
    'extension_configs': {
        'markdown.extensions.headerid':   {
            'level': 1
        },
        'markdown.extensions.codehilite': {
            'css_class': 'highlight',
            'linenums': True
        },
        'markdown.extensions.toc': {
            'title': "Table of contents",
            #'anchorlink': True,
        },
    },
    'output_format': 'html5',
}
