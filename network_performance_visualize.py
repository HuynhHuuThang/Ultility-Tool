import os
import matplotlib.pyplot as plt

def get_speed_data_from_files():
    # Get the list of files in the log directory
    log_dir = './log/download'
    files = os.listdir(log_dir)

    # Initialize empty lists for download speeds and file names
    download_speeds = []
    file_names = []

    # Iterate over the files
    for file in files:
        # Read the download speed from each file
        with open(os.path.join(log_dir, file), 'r') as f:
            download_speed = float(f.read())
            download_speeds.append(download_speed)
            file_names.append(file)

    return download_speeds, file_names

# Get the download speeds and file names
download_speeds, file_names = get_speed_data_from_files()

# Create a bar chart to visualize the download speeds
plt.bar(file_names, download_speeds)
plt.ylabel('Download Speed (Mbps)')
plt.xlabel('File')
plt.title('Network Performance')

# Rotate the x-axis labels for better readability
plt.xticks(rotation=45)

# Display the chart
plt.show()