# pip install ntplib
import ntplib
import time

your_ntp_server = 'raspberrypi4.local'
your_ntp_server = 'raspberrypi.local'


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