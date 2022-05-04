# Tool Auto change tor ip
Automatically change tor ip address over time and using privoxy when accessing the internet. Make it private and safe for you.

> Currently the tool is supported on MacOS and Kali Linux / Ubuntu (No support for Linux versions installed through the Microsoft Store)

# Architecture
<img width="869" alt="image" src="https://user-images.githubusercontent.com/31820707/142816893-8cbdf678-8bd7-4ecd-a639-3bc741b872e7.png">

# PreConfig for Privoxy
1. Edit `/etc/privoxy/config` at `4.1` add `listen-address 127.0.0.1:9050`

# Usage
1. Git clone https://github.com/noobpk/auto-change-tor-ip.git
1. cd auto-change-tor-ip/
1. python3 autorip.py
1. set time and loop
1. add socket 127.0.0.1:9050 into browser or network

# Configure burp suite walk through browser
1. add socket 127.0.0.1:9050 into Network setting -> SOCKS Host in browser
2. add socket 127.0.0.1:9050 into User options -> SOCKS Proxy in burp suite

# Configure autorip with proxychains
1. Edit `/etc/proxychains.conf` at `[ProxyList]` add `socks4 127.0.0.1 9050`

# Interface Autorip when running
<img width="664" alt="image" src="https://user-images.githubusercontent.com/31820707/142809533-8e1034ed-cde1-483f-a363-1749d9b6e755.png">

# Demo
|Name|Link|
|----|----|
|Automation change tor ip address &#124; Basic Usage &#124; Tor - Privoxy - Bypass Firewall  Block Ip| https://youtu.be/GxnUKkYEHcw |
|Automation change tor ip address &#124; Advance Usage &#124; Burp Suite - Nmap - Bypass Firewall  Block Ip| https://youtu.be/X4avfaYWGtw |
