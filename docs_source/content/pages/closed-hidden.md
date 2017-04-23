Title: Closing or hidding comments
Date: 2017-04-23 10:00
Slug: closing-or-hidding-comments
pcs: hidden

On a per article/page basis you can decide to either show, close or hide the comment section.
Just set the `pcs` meta tag to either `open` (default), `closed` or `hidden`.


:Tab: Open
* (Old) Comments **are** visible
* Visitors **can** post new comments

Article/Page:

	#!Markdown
	Title: My Article or Page Title
	pcs: open

Example: [Article with open comments]({filename}/articles/examples/article-open.md)

:Tab: Closed

* (Old) Comments **are** visible
* Visitors can **not** post new comments

Article/Page:

	#!Markdown
	Title: My Article or Page Title
	pcs: closed

Example: [Article with closed comments]({filename}/articles/examples/article-closed.md)

:Tab: Hidden

* (Old) Comments are **not** visible
* Visitors can **not** post new comments

Article/Page:

	#!Markdown
	Title: My Article or Page Title
	pcs: hidden

Example: [Article with hidden comments]({filename}/articles/examples/article-hidden.md)
:TabsEnd:
