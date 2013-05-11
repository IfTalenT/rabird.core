#!/usr/bin/env python

import os
import os.path
import sys
import shutil
import logging
import fnmatch
import src.rabird.logging as rabird_logging
from src.rabird import __version__, distutils
from setuptools import setup, find_packages

from_package = 'src'
to_package = 'rabird'

rabird_logging.load_basic_config_from_environment()

# Convert source to v2.x if we are using python 3.x.
distutils.preprocess_sources_for_compatible(from_package, os.path.realpath(os.curdir))

# Exclude the original source package, only accept the preprocessed package!
our_packages = find_packages(exclude=[from_package, '{}.*'.format(from_package)])

our_requires = [
	'six>=1.3.0'
	]

if sys.platform == "win32":
	our_requires.append('pywin32>=218')

setup(
	name=to_package,
	version=__version__,
	author='HongShe Liang',
	author_email='starofrainnight@gmail.com',
	url='',
	py_modules=[to_package],
	description='{} utilities'.format(to_package),
	long_description=open('README', 'r').read(),
	classifiers=[
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 3',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: BSD License',
		'Topic :: Software Development :: Libraries',
		'Topic :: Utilities',
	],
	install_requires=our_requires,
    packages=our_packages,
    namespace_packages = ['rabird'],
	)
