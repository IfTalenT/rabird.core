#!/usr/bin/env python

from ez_setup import use_setuptools
use_setuptools()

import os
import os.path
import sys
import shutil
import logging
import fnmatch
import src.rabird.core.logging as rabird_logging
from src.rabird.core import __version__, distutils
from setuptools import setup, find_packages

from_package = 'src'
to_package = 'rabird'
package_name = 'rabird.core'

rabird_logging.load_default_config()

# Convert source to v2.x if we are using python 3.x.
distutils.preprocess_sources_for_compatible(from_package, os.path.realpath(os.curdir))

# Exclude the original source package, only accept the preprocessed package!
our_packages = find_packages(exclude=[from_package, '%s.*' % from_package])

our_requires = [
	'six>=1.3.0'
	]

if sys.platform == "win32":
	our_requires.append('pywin32>=218')
else:
	our_requires.append('linux-metrics')

setup(
	name=package_name,
	version=__version__,
	author='Hong-she Liang',
	author_email='starofrainnight@gmail.com',
	url='',
	py_modules=[to_package],
	description='%s utilities' % package_name,
	classifiers=[
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 3',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Topic :: Software Development :: Libraries',
	],
	install_requires=our_requires,
    packages=our_packages,
    namespace_packages = ['rabird'],
	)

