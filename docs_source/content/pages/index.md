Title: Pelican Comment System
Date: 2017-03-28 13:30
Slug: pelican-comment-system
pcs: hidden
save_as: index.html

![.][shields-pelican]
![.][shields-pelican-version]
[![.][shields-pypi-version]](https://pypi.python.org/pypi/pelican_comment_system)
![.][shields-maintenance]

Pelican Comment System is a plugin for [pelican](https://blog.getpelican.com)
and allows you to add **static** comments to your articles and pages.

Comments are stored in files in formats that can be processed by Pelican (e.g., Markdown and reStructuredText).
Each comment resides in its own file.


## Features
* Static comments for each article/page
* Replies to comments
* Avatars and [Identicons](https://en.wikipedia.org/wiki/Identicon)
* Comment Atom feed for each article/page
* Easy styleable via themes
* Comments can be closed or hidden for each article/page separately
* Supports:
	* Python: 2.7 and 3 (3.3 - 3.6)
	* Pelican: 3.4 and newer


## Instructions
* [Getting Started]({filename}getting-started.md)
* [Settings]({filename}settings.md)
* Features:
	* [Avatars and identicons]({filename}avatars.md)
	* [Feeds]({filename}feeds.md)
	* [Closing or hidding comments]({filename}closed-hidden.md)
* [Importing Comments]({filename}importing.md) [from other Blog/Comment Systems]
* For Developers:
	* [Theme Development]({filename}theme-developers.md)
	* [Plugin Development]({filename}plugin-developers.md)


## Requirements

* Pelican 3.4 or newer
* Pillow/PIL [optional, used to create identicons]

[shields-link-pypi]:       https://pypi.python.org/pypi/pelican_comment_system
[shields-pypi-version]:    https://img.shields.io/pypi/v/pelican_comment_system.svg         "PyPI: the Python Package Index"
[shields-maintenance]:     https://img.shields.io/maintenance/yes/2017.svg                  "Maintenance shield"
[shields-pelican]:         https://img.shields.io/badge/Pelican-Plugin-green.svg            "Pelican Plugin"
[shields-pelican-version]: https://img.shields.io/badge/Pelican_Version-3.4_and_newer-yellowgreen.svg "Pelican Version 3.4 and newer"
