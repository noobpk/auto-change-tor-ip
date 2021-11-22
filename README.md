# Tool Auto change tor ip
Automatically change tor ip address over time and using privoxy when accessing the internet. Make it private and safe for you.

> Currently the tool is supported on MacOS and Kali Linux / Ubuntu

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
Basic usage: https://youtu.be/m_q6HNt-X6E

With Proxychains: https://youtu.be/GauKYLUNiFc
