import speedtest
import logging
from datetime import datetime

timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
log_filename=f'wifi_speed_{timestamp}.log'
# Configure logging
logging.basicConfig(filename=log_filename, level=logging.INFO, 
                    format='%(asctime)s - %(message)s')

def log_wifi_speed(fname):
    filename=fname
    # Create a Speedtest object
    st = speedtest.Speedtest(secure=True)
    # Get best server based on ping
    st.get_best_server()
    
    # Perform download and upload speed tests
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps
    ping = st.results.ping
    # Save data to a text file
    with open(f'data_{filename}.txt', 'a') as file:
        file.write(f'Download speed: {download_speed:.2f} Mbps\n')
        file.write(f'Upload speed: {upload_speed:.2f} Mbps\n')
        file.write(f'Ping: {ping:.2f} ms\n')
    # Log the results
    logging.info(f'Download speed: {download_speed:.2f} Mbps')
    logging.info(f'Upload speed: {upload_speed:.2f} Mbps')
    logging.info(f'Ping: {ping:.2f} ms')
def log_down_up_ping_speed(location, dname, upname ,pingname , download_folder_path, upload_folder_path, ping_folder_path):
    download_filename=dname
    upload_filename=upname
    ping_filename=pingname
    location_name=location
    # Create a Speedtest object
    st = speedtest.Speedtest(secure=True)
    # Get best server based on ping
    st.get_best_server()
    
    # Perform download speed test
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    # Perform upload speed test
    upload_speed = st.upload() / 1_000_000 
    #Perform ping test
    ping = st.results.ping
    # Save data to a text file
    with open(f'{download_folder_path}/data_{download_filename}.txt', 'a') as file:
        file.write(f'Location: {location_name}\n')
        file.write(f'Download speed: {download_speed:.2f} Mbps\n')
        file.write("-" * 30 + "\n")
    with open(f'{upload_folder_path}/data_{upload_filename}.txt', 'a') as file:
        file.write(f'Location: {location_name}\n')
        file.write(f'Upload speed: {upload_speed:.2f} Mbps\n')
        file.write("-" * 30 + "\n")
    with open(f'{ping_folder_path}/data_{ping_filename}.txt', 'a') as file:
        file.write(f'Location: {location_name}\n')
        file.write(f'Ping: {ping:.2f} ms\n')
        file.write("-" * 30 + "\n")
if __name__ == "__main__":
    location_name = input("Enter the location name: ")
    filename = location_name + '_wifi_speed.txt'
    # Specify the folder path
    download_log_folder_path = './log/download'
    upload_log_folder_path = './log/upload'
    ping_log_folder_path = './log/ping'
    #specify the log file names
    download_log_name = location_name + '_download_speed.txt'
    upload_log_name = location_name + '_upload_speed.txt'
    ping_log_name = location_name + '_ping_speed.txt'
    logging.info(f'Location: {location_name}')
    with open(f'{ping_log_folder_path}/data_{filename}', 'a') as file:
        file.write(f'Location: {location_name}\n')
    with open(f'data_{filename}.txt', 'a') as file:
        file.write(f'Location: {location_name}\n')
    log_wifi_speed(filename)
    log_down_up_ping_speed(location_name, download_log_name, upload_log_name, ping_log_name, download_log_folder_path, upload_log_folder_path, ping_log_folder_path)
  