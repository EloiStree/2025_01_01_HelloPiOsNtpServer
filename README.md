
# Hello Pi Os Ntp Server  

Code and tutorial to enable an NTP server on your Raspberry Pi to synchronize the time of devices connected to it (with Unity3D for example)

As part of a local multiplayer concept, and the apint.io project, I need an NTP server to run offline on the Raspberry Pi.  
This will ensure that the game remains synchronized to the same time with a delay of only 1–2 milliseconds (max 100 ms).

For Unity3D you can use my tool here 📦:   
NTP: https://github.com/EloiStree/2024_07_07_UnityFetchOffsetNTP  


-------------


Check that the Raspberry Pi is updated
```
sudo apt update && sudo apt upgrade -y
```

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
sudo timedatectl set-timezone Europe/Brussels
ntpq -p
```

Enable if not already enable
```
sudo systemctl enable ntp
```

Restart the server to be sure it is started
```
sudo systemctl restart ntp
```

Open the port of the raspberry pi:
```
sudo ufw allow 123/udp
```

**On Window**:

Check that the pi work by going on your Window device and in admin command line type:  
`ping raspberrypi4.local` Change with your hostname. 


Run this python script:  
```pip install ntplib```
  
``` py
# pip install ntplib
import ntplib
import time

your_ntp_server = 'raspberrypi.local'
your_ntp_server = 'raspberrypi4.local'


def get_ntp_offset(ntp_server: str):
    # Create an NTP client
    client = ntplib.NTPClient()

    try:
        # Request time from the NTP server
        response = client.request(ntp_server)
        
        # Calculate the offset in seconds (difference between local time and server time)
        offset = response.offset
        
        # Convert offset to a more readable format (in seconds)
        print(f"Offset from {ntp_server}: {offset} seconds")
        return offset
    except Exception as e:
        print(f"Error accessing NTP server {ntp_server}: {e}")
        return None

if __name__ == "__main__":
    # NTP server address for Raspberry Pi

    # Get the offset from the Raspberry Pi NTP server
    offset = get_ntp_offset(your_ntp_server)
    
    # Additional: Check if offset is acceptable or out of tolerance
    if offset is not None:
        if abs(offset) > 1:
            print("Warning: Offset is greater than 1 second.")
        else:
            print("Offset is within acceptable range.")
```

It works and you are coding a Unity3D game ?   
`https://github.com/EloiStree/OpenUPM_UnityFetchOffsetNTP.git`   

You can use this script: `NtpOffsetOnlyOnceMono`  
[![image](https://github.com/user-attachments/assets/2afa1c19-00d5-40ef-a96f-a0f52d489580)](https://github.com/EloiStree/OpenUPM_UnityFetchOffsetNTP.git)  




You can add a time routine on the PI:
```
sudo crontab -e
```
That run every 10 a NTP restart to be sure
```
*/10 * * * * /usr/bin/sudo /usr/sbin/service ntp restart

```

Let's check it: 
```
sudo crontab -l
sudo systemctl start cron

```



https://network-tools.webwiz.net/ntp-server-test.htm

[![image](https://github.com/user-attachments/assets/e799cd14-99d0-4956-8c17-dc6e40ea98e2)](https://network-tools.webwiz.net/ntp-server-test.htm)  
[![image](https://github.com/user-attachments/assets/42ada16f-27c8-4958-9b59-e3586729e81c)](https://network-tools.webwiz.net/ntp-server-test.htm)  

