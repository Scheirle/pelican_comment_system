# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import pelican_comment_system

AUTHOR = "Test Author"
SITEURL = "http://example.org"
LOCALE = 'en_US.UTF-8'
TIMEZONE = 'UTC'
DEFAULT_LANG = 'en'

# Paths
PATH = 'content'
ARTICLE_PATHS = ['articles']
PAGE_PATHS = ['pages']

# URLs
AUTHOR_URL = None
AUTHOR_SAVE_AS = ""
CATEGORY_URL = None
CATEGORY_SAVE_AS = ""

# Feeds
AUTHOR_FEED_RSS = None
AUTHOR_FEED_ATOM = None
CATEGORY_FEED_RSS = None
CATEGORY_FEED_ATOM = None
FEED_ALL_RSS = None
FEED_ALL_ATOM = None
FEED_ATOM = None
FEED_RSS = None
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None

# Theme
THEME='theme'
DIRECT_TEMPLATES = []

# Plugins
PLUGINS = [pelican_comment_system]

PELICAN_COMMENT_SYSTEM = {
    'IDENTICON': {
        'DATA': ()
    }
}
