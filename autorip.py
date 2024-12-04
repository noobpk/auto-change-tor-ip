#!/usr/local/bin/python3
import time
import os
import sys
import ssl
from python_socks.sync import Proxy
import random
from log import *
import subprocess
import gevent.monkey
gevent.monkey.patch_all()

print(r'''\033[1;31m \n
              _             _       
             | |           (_)      
   __ _ _   _| |_ ___  _ __ _ _ __  
  / _` | | | | __/ _ \| '__| | '_ \ 
 | (_| | |_| | || (_) | |  | | |_) |
  \__,_|\__,_|\__\___/|_|  |_| .__/ 
                             | |    
                             |_|    
    Automatically Change Tor Ip Address
''')

print(r"\033[1;34m[*]___author___: @noobpk\033[1;37m")
print(r"\033[1;34m[*]___version___: 1.4 dev\033[1;37m")
print(r"")


def detect_platform():
    try:
        platforms = {
            'linux': 'Linux',
            'linux1': 'Linux',
            'linux2': 'Linux',
            'darwin': 'OS X',
        }
        if sys.platform not in platforms:
            logger.error("[x_x] Your platform currently does not support.")
            sys.exit(0)
    except Exception as e:
        logger.error(
            "[x_x] Something went wrong, please check your error message.\n Message - {0}".format(e))

def check_current_ip():
    currentip = subprocess.check_output(
        'curl -s http://ipecho.net/plain || echo "Failed to retrieve IP"',
        shell=True,
        text=True  # Ensures the output is returned as a string instead of bytes
    ).strip()  # Removes any extra newlines or spaces
    return currentip

def check_exists_tor_ip(ipTor):
    with open('listip.txt', 'r') as read_obj:
        for line in read_obj:
            if ipTor in line:
                return True
            else:
                return False

def check_tor_ip():
    server_check = [
        {'host': 'ipecho.net', 'port': 443, 'path': '/plain'},
        {'host': 'check-host.net', 'port': 443, 'path': '/ip'},
        {'host': 'checkip.amazonaws.com', 'port': 443, 'path': '/'},
        {'host': 'api.ipify.org', 'port': 443, 'path': '/'},
        {'host': 'api-bdc.net/data/client-ip', 'port': 443, 'path': '/'},
    ]
    try:
        # Randomly select a server
        selected_server = random.choice(server_check)

        # Extract host, port, and path from the selected server
        dest_host = selected_server['host']
        dest_port = selected_server['port']
        path = selected_server['path']

        # Set up the proxy for Tor
        proxy = Proxy.from_url('socks5://127.0.0.1:9050')
        sock = proxy.connect(dest_host=dest_host, dest_port=dest_port)

        # Wrap the socket with SSL
        sock = ssl.create_default_context().wrap_socket(
            sock=sock,
            server_hostname=dest_host
        )
        
        # Prepare the GET request
        request = (
            f"GET {path} HTTP/1.1\r\n"
            f"Host: {dest_host}\r\n"
            f"Connection: close\r\n\r\n"
        ).encode('utf-8')

        # Send the request
        sock.sendall(request)

        # Receive the response
        response = b""
        while True:
            chunk = sock.recv(4096)
            if not chunk:
                break
            response += chunk

        # Decode the response and extract the IP address
        response = response.decode('utf-8')
        ip = response.split("\r\n\r\n", 1)[1].strip()  # Extract content after headers
        # print(f"Your Tor IP address from {dest_host}: {ip}")
        return dest_host, ip
    
    except Exception as e:
        logger.error(
            "[x_x] Something went wrong, please check your error message.\n Message - {0}".format(e))


def check_runon_osx():
    try:
        istor = os.system('command -v tor 1> /dev/null')
        istorsocks = os.system('command -v torsocks 1> /dev/null')
        isprivoxy = os.path.isdir("/usr/local/Cellar/privoxy")
        file_listip = os.path.isfile("listip.txt")
        if (istor != 0):
            logger.info("Installing Tor...")
            os.system('brew install tor')
            check_runon_osx()
        if (istorsocks != 0):
            logger.info("[+] Installing TorSocks...")
            os.system('brew install torsocks')
            check_runon_osx()
        if (isprivoxy == False):
            logger.info("[+] Installing Privoxy...")
            os.system('brew install privoxy')
            check_runon_osx()
        if (file_listip == False):
            logger.info("[+] Creating File listip.txt")
            open("listip.txt", "w")
            check_runon_osx()
        else:
            logger.info("[*] Dependent Tool: Tor, TorSocks, Privoxy has been installed")
            logger.info("[*] File listip.txt has been created")
            startservice_osx()
    except Exception as e:
        logger.error(
            "[x_x] Something went wrong, please check your error message.\n Message - {0}".format(e))


def startservice_osx():
    try:
        currentip = check_current_ip()
        logger.info(f"[*] Your Current IP Addresss: {currentip}")
        logger.info("[*] Start service Tor")
        os.system("brew services start tor 1> /dev/null")
        time.sleep(2)
        logger.info("[*] Start service Privoxy")
        os.system("brew services start privoxy 1> /dev/null")
        time.sleep(2)
        logger.info("[*] Add to your browsers HTTP Proxy 127.0.0.1:8118")
        logger.info("[*] Access Privoxy Manager http://p.p/")
        logger.info("[+] Set time stamp")
        sec = int(
            input("[?] Time to auto change ip by second (default 600s):") or "600")
        loop = int(input("[?] Number of loop (default 144):") or "144")
        for i in range(loop):
            logger.info("[*] Change New IP")
            os.system("brew services restart tor 1> /dev/null")
            time.sleep(2)
            result = check_tor_ip()
            if check_exists_tor_ip(result[1]):
                restart_tor_service_osx()
            else:
                with open('listip.txt', 'a+') as f:
                    f.write(result[1] + '\n')
                logger.info("[*] Successfully - Your IP has been Changed")
                logger.info(f"[*] New IP Addresss from {result[0]}: {result[1]}")
            time.sleep(sec)
        logger.info("[#] The loop has finished refreshing it")
        stopservice_osx()
    except Exception as e:
        logger.error(
            "[x_x] Something went wrong, please check your error message.\n Message - {0}".format(e))


def restart_tor_service_osx():
    logger.warning("Your IP Already Exist - Request New IP")
    os.system("brew services restart tor 1> /dev/null")
    result = check_tor_ip()
    if check_exists_tor_ip(result[1]):
        restart_tor_service_osx()
    else:
        with open('listip.txt', 'a+') as f:
            f.write(result[1] + '\n')
        logger.info("[*] Successfully - Your IP has been Changed")
        logger.info(f"[*] New IP Addresss from {result[0]}: {result[1]}")

def stopservice_osx():
    try:
        logger.info("[+] Stop service Tor")
        os.system("brew services stop tor 1> /dev/null")
        time.sleep(2)
        logger.info("[+] Stop service Privoxy")
        os.system("brew services stop privoxy 1> /dev/null")
        os.system("clear")
    except Exception as e:
        logger.error(
            "[x_x] Something went wrong, please check your error message.\n Message - {0}".format(e))


def check_runon_linux():
    try:
        logger.info("[+] Check Requirement")
        istor = os.system('command -v tor 1> /dev/null')
        istorsocks = os.system('command -v torsocks 1> /dev/null')
        isprivoxy = os.system('command -v privoxy 1> /dev/null')
        file_listip = os.path.isfile("listip.txt")
        if (os.geteuid() != 0):
            logger.error(
                "[x_x] You need to have root privileges to run this script")
            sys.exit(0)
        if (istor != 0):
            logger.info("[+] Installing Tor")
            os.system('apt-get install tor -y')
            check_runon_linux()
        if (istorsocks != 0):
            logger.info("[+] Installing TorSocks")
            os.system('apt-get install torsocks -y')
            check_runon_linux()
        if (isprivoxy != 0):
            logger.info("[+] Installing Privoxy")
            os.system('apt-get install privoxy -y')
            check_runon_linux()
        if (file_listip == False):
            logger.info("[+] Creating File listip.txt")
            open("listip.txt", "w")
            check_runon_linux()
        else:
            logger.info("[*] Tor has been install")
            logger.info("[*] TorSocks has been install")
            logger.info("[*] Privoxy has been install")
            logger.info("[*] File listip.txt has been created")
            startservice_linux()
    except Exception as e:
        logger.error(
            "[x_x] Something went wrong, please check your error message.\n Message - {0}".format(e))


def startservice_linux():
    try:
        currentip = check_current_ip()
        logger.info(f"[*] Your Current IP Addresss: {currentip}")
        logger.info("[*] Start service Tor")
        os.system("service tor start 1> /dev/null")
        time.sleep(2)
        logger.info("[*] Start service Privoxy")
        os.system("service privoxy start 1> /dev/null")
        time.sleep(2)
        logger.info("[*] Add to your browsers HTTP Proxy 127.0.0.1:8118")
        logger.info("[*] Access Privoxy Manager http://p.p/")
        logger.info("[*] Set time stamp")
        sec = int(
            input("[?] Time to auto change ip by second (default 600s):") or "600")
        loop = int(input("[?] Number of loop (default 144):") or "144")
        for i in range(loop):
            logger.info("[*] Change New IP")
            os.system("service tor restart 1> /dev/null")
            time.sleep(2)
            result = check_tor_ip()
            if check_exists_tor_ip(result[1]):
                restart_tor_service_linux()
            else:
                with open('listip.txt', 'a+') as f:
                    f.write(result[1] + '\n')
                logger.info("[*] Successfully - Your IP has been Changed")
                logger.info(f"[*] New IP Addresss from {result[0]}: {result[1]}")
            time.sleep(sec)
        logger.info("[#] The loop has finished refreshing it")
        stopservice_linux()
    except Exception as e:
        logger.error(
            "[x_x] Something went wrong, please check your error message.\n Message - {0}".format(e))


def restart_tor_service_linux():
    logger.warning("Your IP Already Exist - Request New IP")
    os.system("service tor restart 1> /dev/null")
    result = check_tor_ip()
    if check_exists_tor_ip(result[1]):
        restart_tor_service_linux()
    else:
        with open('listip.txt', 'a+') as f:
            f.write(result[1] + '\n')
        logger.info("[*] Successfully - Your IP has been Changed")
        logger.info(f"[*] New IP Addresss from {result[0]}: {result[1]}")

def stopservice_linux():
    try:
        logger.info("[*] Stop service Tor")
        os.system("service tor stop 1> /dev/null")
        time.sleep(2)
        logger.info("[*] Stop service Privoxy")
        os.system("service privoxy stop 1> /dev/null")
        os.system("clear")
    except Exception as e:
        logger.error(
            "[x_x] Something went wrong, please check your error message.\n Message - {0}".format(e))


def main():
    try:
        detect_platform()
        if (sys.platform == 'darwin'):
            logger.info("[*] Platform: Darwin - MAC OS-X")
            check_runon_osx()
        if (sys.platform == 'linux') | (sys.platform == 'linux1') | (sys.platform == 'linux2'):
            logger.info("[*] Platform: Linux - KALI LINUX - UBUNTU")
            check_runon_linux()
    except KeyboardInterrupt:
        logger.warning("[#] KeyboardInterrupt")
    if (sys.platform == 'darwin'):
        stopservice_osx()
    if (sys.platform == 'linux') | (sys.platform == 'linux1') | (sys.platform == 'linux2'):
        stopservice_linux()


if __name__ == '__main__':
    if sys.version_info < (3, 0):
        logger.error("[x_x] Autorip requires Python 3.x")
    else:
        main()
