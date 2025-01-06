
# 2025_01_01_HelloPiOsNtpServer  
Code and tutorial to enable an NTP server on your Raspberry Pi to synchronize the time of devices connected to it.

As part of a local multiplayer concept, I need an NTP server to run offline on the Raspberry Pi.  
This will ensure that the game remains synchronized to the same time with a delay of only 1–2 milliseconds.  

You are going to look for something like this;)  
NTP: https://github.com/EloiStree/2024_07_07_UnityFetchOffsetNTP  


-------------


```

sudo apt update && sudo apt upgrade -y
rm /git/ntp_server -r
git clone https://github.com/EloiStree/2025_01_01_HelloPiOsNtpServer.git /git/ntp_server/
sudo apt install ntp -y
sudo systemctl status ntp

sudo nano /etc/ntp.conf
// For anywhere
pool 0.debian.pool.ntp.org iburst
pool 1.debian.pool.ntp.org iburst
pool 2.debian.pool.ntp.org iburst
pool 3.debian.pool.ntp.org iburst

// or For belgium
server 0.be.pool.ntp.org iburst
server 1.be.pool.ntp.org iburst
server 2.be.pool.ntp.org iburst
server 3.be.pool.ntp.org iburst

// Only your computer
restrict 192.168.1.0 mask 255.255.255.0 nomodify notrap

// for all
restrict 0.0.0.0 mask 0.0.0.0 nomodify notrap


ntpq -p
sudo timedatectl set-timezone Europe/Brussels

sudo systemctl enable ntp
sudo systemctl restart ntp

```

to open port:  123.


