#!/usr/bin/env python
# setup
# Setup script for cellular-automata
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Fri Jan 31 09:15:08 2014 -0500
#
# Copyright (C) 2014 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: setup.py [] benjamin@bengfort.com $

"""
Setup script for cellular-automata
"""

##########################################################################
## Imports
##########################################################################

try:
    from setuptools import setup
    from setuptools import find_packages
except ImportError:
    raise ImportError("Could not import \"setuptools\"."
                      "Please install the setuptools package.")

##########################################################################
## Package Information
##########################################################################

packages = find_packages(where=".", exclude=("tests", "bin", "docs", "fixtures",))
requires = []

with open('requirements.txt', 'r') as reqfile:
    for line in reqfile:
        requires.append(line.strip())

classifiers = (
    'Development Status :: 3 - Alpha',
    'Environment :: MacOS X',
    'Environment :: Console',
    'Environment :: Other Environment',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: POSIX :: Linux',
    'Programming Language :: Python :: 2.7',
    'Topic :: Multimedia :: Graphics',
    'Topic :: Artistic Software',
    'Topic :: Scientific/Engineering :: Visualization',
    'Topic :: Scientific/Engineering :: Artificial Life',
)

config = {
    "name": "PyCellularAutomata",
    "version": "0.2",
    "description": "a Python Cellular Automata visualization library",
    "author": "Benjamin Bengfort",
    "author_email": "benjamin@bengfort.com",
    "url": "https://github.com/bbengfort/cellular-automata",
    "packages": packages,
    "install_requires": requires,
    "classifiers": classifiers,
    "zip_safe": False,
    "scripts": ["bin/pyca",],
}

##########################################################################
## Run setup script
##########################################################################

if __name__ == '__main__':
    setup(**config)
