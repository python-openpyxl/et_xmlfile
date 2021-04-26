#!/usr/bin/env python

"""Setup script for packaging et_xmfile.
"""
import sys
import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
try:
    with open(os.path.join(here, 'README.rst')) as f:
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
    packages=find_packages(
        exclude=["*.tests",]
    ),
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
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7',
                 'Programming Language :: Python :: 3.8',
                 'Programming Language :: Python :: 3.9',
                 ],
    )
