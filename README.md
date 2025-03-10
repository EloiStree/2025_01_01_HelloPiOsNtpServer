
# 2025_01_01_HelloPiOsNtpServer  
Code and tutorial to enable an NTP server on your Raspberry Pi to synchronize the time of devices connected to it.

As part of a local multiplayer concept, I need an NTP server to run offline on the Raspberry Pi.  
This will ensure that the game remains synchronized to the same time with a delay of only 1–2 milliseconds.  

You are going to look for something like this;)  
NTP: https://github.com/EloiStree/2024_07_07_UnityFetchOffsetNTP  


-------------


Check that the Raspberry Pi is updated
```sudo apt update && sudo apt upgrade -y```

Install the manual in case you need to find it later
```
rm /git/ntp_server -r
git clone https://github.com/EloiStree/2025_01_01_HelloPiOsNtpServer.git /git/ntp_server/
```

Install the NTP tool on the PI and check it status
```
sudo apt install ntp -y
sudo systemctl status ntp
```
Open and edit the ntp config file to set the source
```
sudo nano /etc/ntp.conf
```

Copy the following depending on your country  
  
For world synchronisation  
```
pool 0.debian.pool.ntp.org iburst
pool 1.debian.pool.ntp.org iburst
pool 2.debian.pool.ntp.org iburst
pool 3.debian.pool.ntp.org iburst
```
  
For belgium synchronisation  
```
server 0.be.pool.ntp.org iburst
server 1.be.pool.ntp.org iburst
server 2.be.pool.ntp.org iburst
server 3.be.pool.ntp.org iburst
```


Copy this n the config to allows anyone to connect to it.  
```
restrict 0.0.0.0 mask 0.0.0.0 nomodify notrap
```

Check the peer server and set timezone to brussels (if in Belgium)
```
ntpq -p
sudo timedatectl set-timezone Europe/Brussels
```

Enable if not already enable
```
sudo systemctl enable ntp
```

Restart the server to be sure it is started
```
sudo systemctl restart ntp
```



