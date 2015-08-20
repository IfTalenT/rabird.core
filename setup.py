#!/usr/bin/env python

from ez_setup import get_best_downloader

downloader = get_best_downloader()

try:
    import pip
except:
    # If we do not have pip, we fetch and install one. It will also install
    # setuptools and wheel. 
    downloader("https://bootstrap.pypa.io/get-pip.py", "get-pip.py")
    exec(open("get-pip.py").read())

import os
import os.path
import sys
import shutil
import logging
import fnmatch

# First remove "./rabird" directory, otherwise it would failed to import
# global rabird.core.
shutil.rmtree("./rabird", ignore_errors=True)

from src.rabird.core import __version__, distutils
from setuptools import setup, find_packages

package_name = "rabird.core"

# Convert source to v2.x if we are using python 2.x.
source_dir = distutils.preprocess_source()

# Exclude the original source package, only accept the preprocessed package!
our_packages = find_packages(where=source_dir)
    
our_requires = [
    "six>=1.3.0"
    ]

if sys.platform == "win32":
    our_requires.append("pywin32>=218")
else:
    our_requires.append("linux-metrics")
    
if sys.version_info[0] == 2:
    our_requires.append("enum34")
    
long_description=(
     open("README.rst", "r").read()
     + "\n" +
     open("CHANGES.rst", "r").read()
     )

setup(
    name=package_name,
    version=__version__,
    author="Hong-She Liang",
    author_email="starofrainnight@gmail.com",
    url="https://github.com/starofrainnight/%s" % package_name,
    description="A library contained miscellaneous functions and fixes that used during our development",
    long_description=long_description,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",        
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent", 
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: CPython",        
        "Topic :: Software Development :: Libraries",
    ],
    install_requires=our_requires,
    package_dir = {"": source_dir},
    packages=our_packages,
    namespace_packages=[package_name.split(".")[0]],
    # If we don"t set the zip_safe to False, pip can"t find us.
    zip_safe=False,
    )
