Title: Settings
Date: 2017-03-28 18:00
Slug: settings
pcs: hidden

This plugin has a few settings to fine tune its behaviour.
Below is the default configuration listed.

	#!python
	PELICAN_COMMENT_SYSTEM = {
		'DIR': 'comments',
		'IDENTICON': {
			'OUTPUT_PATH': 'images/identicon',
			'DATA': ('author',),
			'SIZE': 72,
		},
		'AUTHORS':  {},
		'FEED':     os.path.join('feeds', 'comment.%s.atom.xml'),
		'FEED_ALL': os.path.join('feeds', 'comments.all.atom.xml'),
		'DEFAULT_STATE': {
			'Article': 'open',
			'Page':    'open',
			'Draft':   'closed',
		}
	}
	COMMENT_URL = '#comment-{slug}'

If you want to adjust something only specify the keys you change in your `pelicanconf.py`, e.g.:

	#!python
	PELICAN_COMMENT_SYSTEM = {
		'DEFAULT_STATE': {
			'Page':    'closed',
		}
	}

Now everthing not specified will be taken from the default configuration, e.g. the `DEFAULT_STATE` for articles is still `open`.

### Settings in-depth

:Tab: DIR
Folder where the comments are stored, relative to `PATH`.

<hr>

In a default pelican installation `PATH` points to `./content/` and therefore `DIR` to `./content/comments/`.

**Pro:** You don't have to exclude the `DIR` from the articles or pages path, the Pelican Comment System already handles that.

:Tab: IDENTICON
`OUTPUT_PATH`:

Relative URL to the output folder where the identicons get stored.
<hr>

`DATA`:

Tuple that contains all metadata tags, which in combination identifie a comment author.

Only if all metadata are the same, two comment files are treated as if written from the same author.

<hr>

`SIZE`:

Width and height of the identicons.
Has to be a multiple of 3.

:Tab: AUTHORS
Comment authors, which should have a specific avatar.
See also [Avatars and Identicons]({filename}avatars.md).

Example:

	#!python
	PELICAN_COMMENT_SYSTEM = {
		'IDENTICON': {
			'DATA': ('author', 'email',)
		}
		'AUTHORS':  {
			('John','john@example.com',): "images/authors/john.png",
			('Tom','tom@example.org',): "images/authors/tom.png",
		}
	}

No identicons will be created for the comment authors John (john@example.com) and Tom (tom@example.org).
Instead the specified avatar will be used.


:Tab: FEED
Relative URL to output the Atom feeds (one feed per article).
`%s` gets replaced with the slug of the article.

Set to `None` to disable the feeds.

:Tab: FEED_ALL
Relative URL to output the all-comments Atom feed.

Set to `None` to disable this feed.

:Tab: DEFAULT_STATE
Default state for articles, pages and drafts.
Valid values are: `open`, `closed` and `hidden`

See [Closing or hidding comments]({filename}closed-hidden.md).

:Tab: COMMENT_URL
`{slug}` gets replaced with the slug of the comment.

This URL has to match the html ids of the comments in your theme.
Example: [Feeds]({filename}feeds.md)

:TabsEnd:
