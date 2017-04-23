Title: Avatars and Identicons
Date: 2017-03-28 18:00
Slug: avatars-and-identicons
pcs: hidden

For avatars and [identicons](https://en.wikipedia.org/wiki/Identicon) support the Python Image Library (`PIL` or `Pillow`) is required.
Make sure it is installed: `pip install Pillow`

By default the Pelican Comment System treats all comments with the same `author` tag as if written from the same person.
And therefore uses the same avatar/identicon for these comments.
See also [In-depth Settings]({filename}settings.md).

## Specific Avatars
To set a specific avatar for a author you have to add them to the `PELICAN_COMMENT_SYSTEM['AUTHORS']` dictionary.

The `key` of the dictionary has to be a tuple of the form of `PELICAN_COMMENT_SYSTEM['IDENTICON']['DATA']`.

The `value` of the dictionary is the path to the specific avatar.

##### Example
```python
PELICAN_COMMENT_SYSTEM = {
	'AUTHORS': {
		('John',): "images/authors/john.png",
		('Tom',): "images/authors/tom.png",
	}
}
```

## Theme
To display the avatars and identicons simply add the following in the "comment for loop" in your theme:

```html
<img src="{{ SITEURL }}/{{ comment.avatar }}"
		alt="Avatar"
		height="{{ PELICAN_COMMENT_SYSTEM_IDENTICON_SIZE }}"
		width="{{ PELICAN_COMMENT_SYSTEM_IDENTICON_SIZE }}">
```

Of cause the `height` and `width` are optional, but they make sure that everything has the same size (in particular  specific avatars).
