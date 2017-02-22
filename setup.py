
import os
import re
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

base_dir = os.path.dirname(os.path.abspath(__file__))


def get_version(filename="pelican_comment_system/__init__.py"):
    with open(os.path.join(base_dir, filename), encoding="utf-8") as initfile:
        for line in initfile.readlines():
            m = re.match("__version__ *= *['\"](.*)['\"]", line)
            if m:
                return m.group(1)


def get_long_description(absolute_url):
    readme = open(os.path.join(base_dir, "README.rst")).read()
    # Fix relative links
    readme = readme.replace("<doc/", "<" + absolute_url + "/doc/")
    readme = readme.replace("<./", "<" + absolute_url + "/")
    # TODO: remove change log section from readme
    return "\n\n".join([readme, open(os.path.join(base_dir, "CHANGELOG.rst")).read()])

base_url = "https://github.com/Scheirle/pelican_comment_system"
setup(
    name="pelican_comment_system",
    version=get_version(),
    description="Allows you to add static comments to your articles on your Pelican blog.",
    long_description=get_long_description(base_url + "/tree/v" + get_version()),
    author="Bernhard Scheirle",
    author_email="bernhard+python@scheirle.de",
    url=base_url,
    packages=['pelican_comment_system',
              'pelican_comment_system.identicon'],
    include_package_data=True,
    install_requires=[
        'pelican>=3.4',
        'pillow',
        ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        # 'Programming Language :: Python :: 3.4',
        # 'Programming Language :: Python :: 3.5',
        # 'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
)
