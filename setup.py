#!/usr/bin/env python

"""Setup script for packaging et_xmfile.

Requires setuptools.

To build the setuptools egg use
    python setup.py bdist_egg
and either upload it to the PyPI with:
    python setup.py upload
or upload to your own server and register the release with PyPI:
    python setup.py register

A source distribution (.zip) can be built with
    python setup.py sdist --format=zip

That uses the manifest.in file for data files rather than searching for
them here.

"""
import codecs
import sys
import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
try:
    with codecs.open(os.path.join(here, 'README.rst'), encoding="utf-8") as f:
        README = f.read()
except IOError:
    README = ''

sys.path.append('')

from et_xmlfile import (
    __author__,
    __license__,
    __author_email__,
    __url__,
    __version__
)


setup(name='et_xmlfile',
    packages=find_packages(),
    # metadata
    version=__version__,
    description="An implementation of lxml.xmlfile for the standard library",
    long_description=README,
    author=__author__,
    author_email=__author_email__,
    url=__url__,
    license=__license__,
    python_requires=">=3.6",
    classifiers=[
                 'Development Status :: 5 - Production/Stable',
                 'Operating System :: MacOS :: MacOS X',
                 'Operating System :: Microsoft :: Windows',
                 'Operating System :: POSIX',
                 'License :: OSI Approved :: MIT License',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2.6',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3.3',
                 'Programming Language :: Python :: 3.4',
                 ],
    )
