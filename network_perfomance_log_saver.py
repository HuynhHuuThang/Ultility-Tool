import speedtest
import logging
from datetime import datetime

timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
log_filename=f'wifi_speed_{timestamp}.log'
# Configure logging
logging.basicConfig(filename=log_filename, level=logging.INFO, 
                    format='%(asctime)s - %(message)s')

def log_wifi_speed():
    # Create a Speedtest object
    st = speedtest.Speedtest(secure=True)
    # Get best server based on ping
    st.get_best_server()
    
    # Perform download and upload speed tests
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps
    ping = st.results.ping
    # Save data to a text file
    with open('data.txt', 'a') as file:
        file.write(f'Download speed: {download_speed:.2f} Mbps\n')
        file.write(f'Upload speed: {upload_speed:.2f} Mbps\n')
        file.write(f'Ping: {ping:.2f} ms\n')
    # Log the results
    logging.info(f'Download speed: {download_speed:.2f} Mbps')
    logging.info(f'Upload speed: {upload_speed:.2f} Mbps')
    logging.info(f'Ping: {ping:.2f} ms')

if __name__ == "__main__":
    location_name = input("Enter the location name: ")
    logging.info(f'Location: {location_name}')
    with open('data.txt', 'a') as file:
        file.write(f'Location: {location_name}\n')
    log_wifi_speed()
