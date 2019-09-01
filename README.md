# Tool Auto change tor ip
Automatically change ip address tor over time when accessing the internet. Make it private and safe for you.

> Currently the tool is supported on MacOS and Kali Linux

# Usage
1. Git clone https://github.com/noobpk/auto-change-tor-ip.git
1. cd auto-change-tor-ip/
1. python3 autorip.py
1. set time and loop
1. add socket 127.0.0.1:9050 into browser or network

# Configure burp suite walk through browser
1. add socket 127.0.0.1:9050 into Network setting -> SOCKS Host in browser
2. add socket 127.0.0.1:9050 into User options -> SOCKS Proxy in burp suite

# Image
<img width="878" alt="image" src="https://user-images.githubusercontent.com/31820707/64080213-dc93de00-cd1b-11e9-9501-1666c2d51e4a.png">
