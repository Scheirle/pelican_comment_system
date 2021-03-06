Pelican Comment System |pypi-version|
=====================================

Pelican Comment System allows you to add static comments to your
articles.

Comments are stored in files in formats that can be processed by Pelican
(e.g., Markdown, reStructuredText). Each comment resides in its own
file.

Features
--------

-  Static comments for each article
-  Replies to comments
-  Avatars and `Identicons <https://en.wikipedia.org/wiki/Identicon>`__
-  Comment Atom feed for each article
-  Easy styleable via themes
-  Python 2 and 3 support

See it in action here:
`bernhard.scheirle.de <http://bernhard.scheirle.de/posts/2014/March/29/static-comments-via-email/>`__

+---------------------+-------------------------------+-------------------------------+
| Author              | Website                       | Github                        |
+=====================+===============================+===============================+
| Bernhard Scheirle   | http://bernhard.scheirle.de   | https://github.com/Scheirle   |
+---------------------+-------------------------------+-------------------------------+

Instructions
------------

-  `Quickstart Guide <doc/quickstart.md>`__
-  `Installation and basic usage <doc/installation.md>`__
-  `Import existing comments <doc/import.md>`__
-  `Avatars and identicons <doc/avatars.md>`__
-  `Comment Atom feed <doc/feed.md>`__
-  `[Developer] How to do a release <doc/how-to-release.md>`__

PyPi
------------
The Pelican Comment System is now also in the Python Package Index and can easily installed via:

::

    pip install pelican_comment_system


Requirements
------------

Pelican 3.4 or newer is required.

To create identicons, the Python Image Library is needed. Therefore you
either need PIL **or** Pillow (recommended).

**Install Pillow via:**

::

    pip install Pillow

If you don't want avatars or identicons, this plugin works fine without
PIL/Pillow. You will, however, see a warning that identicons are
deactivated (as expected).

Change Log
----------

The change log can be found in the `CHANGELOG.rst <./CHANGELOG.rst>`__
file.

.. |pypi-version| image:: https://img.shields.io/pypi/v/pelican_comment_system.svg
   :target: https://pypi.python.org/pypi/pelican_comment_system
   :alt: PyPI: the Python Package Index
