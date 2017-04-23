Title: Getting Started
Date: 2017-03-28 18:00
Slug: getting-started
pcs: hidden

[TOC]

## Installation
You can either use `pip`, `git` or manually download this plugin:

:Tab: Pip
Execute:

	#!bash
	pip install pelican_comment_system

Changes in `pelicanconf.py`:

	#!python
	PLUGINS = ['pelican_comment_system']

:Tab: Git
Execute:

	#!bash
	cd your_plugin_folder
	git clone "git@github.com:Scheirle/pelican_comment_system.git"

[Optional]

	#!bash
	pip install Pillow

Changes in `pelicanconf.py`:

	#!python
	PLUGIN_PATHS = ['your_plugin_folder']
	PLUGINS = ['pelican_comment_system']

:Tab: Download
Manually download the plugin from: <https://github.com/Scheirle/pelican_comment_system/releases>
and extract it into your plugin folder.

[Optional]

	#!bash
	pip install Pillow

Changes in `pelicanconf.py`:

	#!python
	PLUGIN_PATHS = ['your_plugin_folder']
	PLUGINS = ['pelican_comment_system']

:TabsEnd:

### Theme

Your theme needs to support the Pelican Comment System so the comments can be displayed on your site.
You can either use a theme with already built-in support or easily extend your current theme.

:Tab: Extend your current theme

Execute:

	#!bash
	cd your_theme_folder
	mkdir -p ./static/js
	mkdir -p ./templates/pcs

	wget --directory-prefix="./static/js" "https://raw.githubusercontent.com/Scheirle/pelican_comment_system/master/theme/static/js/comments.js"
	wget --directory-prefix="./templates/pcs" "https://raw.githubusercontent.com/Scheirle/pelican_comment_system/master/theme/templates/pcs/comments.html"

Modify your `./templates/article.html` template:

1. Add `{% import 'pcs/comments.html' as pcs with context %}` to the top of the file.
2. Add `{{ pcs.comments_quickstart("emailuser", "example.com") }}` where you want the comments to be displayed.
   For most themes right below `{{ article.content }}` is a good place.
3. Replace `emailuser` and `example.com` with your e-mail address: `emailuser@example.com`

And that's it!
Your site is now ready to display comments.

For an in-depth guide see: [Guide for theme developers]({filename}theme-developers.md)

:Tab: Themes with built-in support
Just install the theme as noted by the theme author and you are ready to go.

List of themes with Pelican Comment System support:

* [Seafoam](https://github.com/MinchinWeb/seafoam)


:TabsEnd:

## Adding a comment to an article or page

### Folder structure

* Every comment gets stored in its own file. The filename does not matter.
* All comments of the same Article/Page are located in the same folder.
* The folder name is equal to the slug of the Article/Page.
* All these folders have to be placed in `content/comments/`.

#### Example

All comments of the article `foo-bar` must be placed in `content/comments/foo-bar/`.

Below is an example folder structure listed with two articles and a total of five comments.

	content
	├── comments
	│   └── foo-bar
	│   │   ├── 1.md
	│   │   └── 0.md
	│   └── some-other-slug
	│       ├── random-Name.md
	│       ├── 1.rst
	│       └── 0.md
	├── foo-bar.md
	└── some-other-slug.md

(The path `content/comments/` can be changed via the settings, see [In-depth Settings]({filename}settings.md))

### Comment file
The comment file itself is very similar to an article or page file and therefore it can be in any format pelican supports.
The only difference is the meta data.

#### Meta data

Tag           | Required  | Description
--------------|-----------|----------------
`date`        | yes       | Date when the comment was posted
`author`      | yes       | Name of the comment author
`slug`        | no        | Slug of the comment. If not present it will be computed from the file name (including the extension)
`replyto`     | no        | Slug of the parent comment

Every other (custom) tag gets parsed as well and will be available through the theme.

##### Example of a (markdown) comment file

	#!markdown
	date: 2014-3-21 15:02
	author: Author of the comment
	website: http://authors.website.com
	replyto: 1md
	anothermetatag: some random tag

	Content of the comment.

