#!/usr/local/bin/python3
import time
import os
import sys

print ('''\033[1;31m \n
_|      _|                      _|                  _|      
_|_|    _|    _|_|      _|_|    _|_|_|    _|_|_|    _|  _|  
_|  _|  _|  _|    _|  _|    _|  _|    _|  _|    _|  _|_|    
_|    _|_|  _|    _|  _|    _|  _|    _|  _|    _|  _|  _|  
_|      _|    _|_|      _|_|    _|_|_|    _|_|_|    _|    _|
        https://noobpk.github.io          _|                 
    Automatically Change Ip Address Tor   _|    #noobteam
''')

print ("\033[1;34m[*]___author___: @noobpk\033[1;37m")
print ("\033[1;34m[*]___version___: 1.0\033[1;37m")
print ("")

def detect_platform():

    platforms = {
    	'linux'  : 'Linux',
    	'linux1' : 'Linux',
        'linux2' : 'Linux',
        'darwin' : 'OS X',
    }
    print ("\033[1;32m[+] Detect Platform\033[1;37m")
    if sys.platform not in platforms:
    	print ("\033[1;31m[x] Your platform currently does not support\033[1;31m")

def runon_osx():

	print ("\033[1;32m[+] Check Requirement\033[1;37m")
	istor = os.system('command -v tor 1> /dev/null')
	isprivoxy = os.path.isdir("/usr/local/Cellar/privoxy")
	if (istor != 0):
		print ("\033[1;32m[+] Installing Tor\033[1;37m")
		os.system('brew install tor')
		runon_osx()
	if (isprivoxy == False):
		print ("\033[1;32m[+] Installing Privoxy\033[1;37m")
		os.system('brew install privoxy')
		runon_osx()
	else:
		print ("\033[1;34m[!] Tor has been install\033[1;37m")
		print ("\033[1;34m[!] Privoxy has been install\033[1;37m")
		osx()

def osx():

	print ("\033[1;32m[+] Start service Tor\033[1;37m")
	os.system("brew services start tor")
	time.sleep(5)
	print ("\033[1;32m[+] Start service Privoxy\033[1;37m")
	os.system("brew services start privoxy")
	time.sleep(5)
	print ("\033[1;34m[!] Change your SOCKES to 127.0.0.1:9050\033[1;37m")
	print ("\033[1;32m[+] Set time stamp\033[1;37m")
	sec = int(input("[?] Time to auto change ip by second (default 600s):") or "600")
	loop = int(input("[?] Number of loop (default 144):") or "144")
	for i in range(loop):  
	      time.sleep(sec)
	      os.system("brew services restart tor")
	      time.sleep(5)
	      print("\033[1;32m[+] Successfully - Your IP has been Changed\033[1;37m")
	print ("\033[1;31m[#] The loop has finished refreshing it\033[1;37m")
	print ("\033[1;32m[+] Stop service Tor\033[1;37m")
	os.system("brew services stop tor")
	time.sleep(5)
	print ("\033[1;32m[+] Stop service Privoxy\033[1;37m")
	os.system("brew services stop privoxy")

def runon_linux():

	print ("\033[1;32m[+] Check Requirement\033[1;37m")
	istor = os.system('command -v tor 1> /dev/null')
	isprivoxy = os.system('command -v privoxy 1> /dev/null')
	if (istor != 0):
		print ("\033[1;32m[+] Installing Tor\033[1;37m")
		os.system('apt-get install tor')
		runon_linux()
	if (isprivoxy != 0):
		print ("\033[1;32m[+] Installing Privoxy\033[1;37m")
		os.system('apt-get install privoxy')
		runon_linux()
	else:
		print ("\033[1;34m[!] Tor has been install\033[1;37m")
		print ("\033[1;34m[!] Privoxy has been install\033[1;37m")
		linux()

def linux():

	print ("\033[1;32m[+] Start service Tor\033[1;37m")
	os.system("service tor start")
	time.sleep(5)
	print ("\033[1;32m[+] Start service Privoxy\033[1;37m")
	os.system("service privoxy start")
	time.sleep(5)
	print ("\033[1;34m[!] Change your SOCKES to 127.0.0.1:9050\033[1;37m")
	print ("\033[1;32m[+] Set time stamp\033[1;37m")
	sec = int(input("[?] Time to auto change ip by second (default 600s):") or "600")
	loop = int(input("[?] Number of loop (default 144):") or "144")
	for i in range(loop):  
	      time.sleep(sec)
	      os.system("service tor restart")
	      time.sleep(5)
	      print("\033[1;32m[+] Successfully - Your IP has been Changed\033[1;37m")
	print ("\033[1;31m[#] The loop has finished refreshing it\033[1;37m")
	print ("\033[1;32m[+] Stop service Tor\033[1;37m")
	os.system("service tor stop")
	time.sleep(5)
	print ("\033[1;32m[+] Stop service Privoxy\033[1;37m")
	os.system("service privoxy stop")

def main():
	
	detect_platform()
	if (sys.platform == 'darwin'):
		print ("\033[1;34m[*] Darwin - MAC OS-X\033[1;37m")
		runon_osx()
	if (sys.platform == 'linux') | (sys.platform == 'linux1') | (sys.platform == 'linux2'):
		print ("\033[1;34m[*] Linux - KALI LINUX\033[1;37m")
		runon_linux()

if __name__ == '__main__':
    main()