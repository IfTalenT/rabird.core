
#--IMPORT_ALL_FROM_FUTURE--#

import time
import win32pipe
import win32file
import pywintypes
import collections
import string
import rabird.gts
import sys

scripter = rabird.gts.create_scripter('securecrt')

print("Wating connection ...")

scripter.connect()

print("Execute commands ...")

try:
	scripter.send('sleep 3; echo hello\n')
	result = scripter.wait_for_strings(['hello'])
	print( 'result : ' + str(result) ) 
	scripter.send_keys('{NUM_9}')
	scripter.send_keys('{NUM_ENTER}')
	scripter._quit()
except ConnectionAbortedError:
	pass

print("Exit ...")
