# -*- coding: UTF-8 -*-

#--IMPORT_ALL_FROM_FUTURE--#

'''
@date 2013-7-7
@author Hong-She Liang <starofrainnight@gmail.com>
'''

import sys

if sys.platform == "win32":
    from .win32 import Keyboard
else:
    from .xdotool import Keyboard
    