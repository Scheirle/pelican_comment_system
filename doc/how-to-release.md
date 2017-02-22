# How to do a release

1. Update the [change log](../CHANGELOG.rst)
2. Create a new git tag:
	* e.g. `git tag -a v1.2.1`
	* e.g. `git push origin v.1.2.1`
3. Package the project
	* Source Distribution: `python setup.py sdist`
	* Universal Wheels: `python setup.py bdist_wheel --universal` (only valid as long as we support python 2 and 3)
	* [Further Help](https://packaging.python.org/distributing/#packaging-your-project)
4. Upload packages:
	* `twine upload dist/*`
	* [Twine Help](https://pypi.python.org/pypi/twine)
5. Add a new heading in the [change log](../CHANGELOG.rst)

# PyPi - Register project [Already done]
`twine register -r testpypi dist/pelican_comment_system-1.4.0-py2.py3-none-any.whl`
