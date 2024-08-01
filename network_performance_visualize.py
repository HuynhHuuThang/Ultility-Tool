import speedtest
import datetime

import matplotlib.pyplot as plt

def run_speed_test():
    # Create a Speedtest object
    st = speedtest.Speedtest()

    # Run the speed test
    st.get_best_server()
    st.download()
    st.upload()

    # Get the results
    results = st.results.dict()

    return results

def export_speed_test_results(results):
    # Get the current date and time
    now = datetime.datetime.now()

    # Create a filename for the log file using the current date and time
    filename = f"speed_test_results_{now.strftime('%Y-%m-%d_%H-%M-%S')}.txt"

    # Open the log file in write mode
    with open(filename, 'w') as file:
        # Write the results to the log file
        file.write(f"Download Speed: {results['download']} bytes/s\n")
        file.write(f"Upload Speed: {results['upload']} bytes/s\n")
        file.write(f"Ping: {results['ping']} ms\n")
        file.write(f"Server: {results['server']['host']} ({results['server']['name']})\n")

    print(f"Speed test results exported to {filename}")


def visualize_speed_test(results):
    # Extract the download and upload speeds from the results
    download_speed = results['download'] / 10**6  # Convert to Mbps
    upload_speed = results['upload'] / 10**6  # Convert to Mbps

    # Create a bar chart to visualize the speeds
    speeds = [download_speed, upload_speed]
    labels = ['Download', 'Upload']
    plt.bar(labels, speeds)
    plt.ylabel('Speed (Mbps)')
    plt.title('Network Performance')

    # Display the chart
    plt.show()

if __name__ == "__main__":
    # Run the speed test and visualize the results
    results = run_speed_test()
    visualize_speed_test(results)
    # Export the results to a log file
    export_speed_test_results(results)
