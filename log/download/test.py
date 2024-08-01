import os

def process_files(log_dir, files, output_file):
    formatted_data = []

    for file in files:
        with open(os.path.join(log_dir, file), 'r') as f:
            lines = f.readlines()
            location = lines[0].split(": ")[1].strip()
            download_speed = lines[1].split(": ")[1].strip().split(" ")[0]
            formatted_data.append(f"{location}={download_speed}")

    with open(output_file, 'w') as f:
        for data in formatted_data:
            f.write(data + "\n")

# Directory containing the log files
log_dir = './'
# List of files to read
files = [
    'data_A1public_download_speed.txt', 'data_A2public_download_speed.txt', 
    'data_A3public_download_speed.txt', 'data_A4public_download_speed.txt', 
    'data_A5public_download_speed.txt', 'data_A6public_download_speed.txt', 
    'data_A7public_download_speed.txt', 'data_A8public_download_speed.txt', 
    'data_A9public_download_speed.txt'
]
# Output file to save the formatted data
output_file = 'formatted_data.txt'

# Process the files and save the formatted data
process_files(log_dir, files, output_file)