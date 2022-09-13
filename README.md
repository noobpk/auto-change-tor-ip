# Tool Auto change tor ip
Automatically change tor ip address over time and using privoxy when accessing the internet. Make it private and safe for you.

> Currently the tool is supported on MacOS and Kali Linux / Ubuntu (No support for Linux versions installed through the Microsoft Store)

# Architecture
![image](https://user-images.githubusercontent.com/31820707/189964620-7062c280-7011-4b13-84a5-bf676e721d25.png)


# PreConfig for Privoxy
1. Linux - Edit `/etc/privoxy/config` 
    - Find & Set `enable-remote-toggle 1`
    - Finf & Set `enable-edit-actions 1`
    - Find & Remove `#` in `forward-socks5t   /               127.0.0.1:9050 .`
2. MacOS - Edit `/usr/local/etc/privoxy/config` 
    - Find & Set `enable-remote-toggle 1`
    - Find & Set `enable-edit-actions 1`
    - Find & Remove `#` in `forward-socks5t   /               127.0.0.1:9050 .`

# Usage
1. Git clone https://github.com/noobpk/auto-change-tor-ip.git
1. cd auto-change-tor-ip/
1. python3 autorip.py
1. set time and loop
1. add HTTP Proxy 127.0.0.1:8118 into browser or network

<!-- # Configure burp suite walk through browser
1. add socket 127.0.0.1:9050 into Network setting -> SOCKS Host in browser
2. On Burp Suite - Add socket 127.0.0.1:9050 into User options -> SOCKS Proxy in burp suite -->

<!-- # Configure autorip with proxychains
1. Edit `/etc/proxychains.conf` at `[ProxyList]` add `socks5 127.0.0.1 9050` -->

# Interface Autorip when running
<img width="664" alt="image" src="https://user-images.githubusercontent.com/31820707/142809533-8e1034ed-cde1-483f-a363-1749d9b6e755.png">

# Demo
|Name|Link|
|----|----|
|Automation change tor ip address &#124; Basic Usage &#124; Tor - Privoxy - Bypass Firewall  Block Ip| https://youtu.be/GxnUKkYEHcw |
|Automation change tor ip address &#124; Advance Usage &#124; Burp Suite - Nmap - Bypass Firewall  Block Ip| https://youtu.be/X4avfaYWGtw |
