import pywifi
from pywifi import const
import time


def get_nearby_wifi_stats():

    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    iface.scan()
    scan_results = iface.scan_results()
    for data in scan_results:
        # print(f"SSID: {data.ssid}")
        # print(f"BSSID: {data.bssid}")
        # print(f"{data.ssid} Signal Strength: {data.signal}")
        # print(f"Frequency: {data.freq} MHz")
        # Save data to a text file
        with open("wifi_nearby_stats.txt", "a") as file:
            for data in scan_results:
                file.write(f"SSID: {data.ssid}\n")
                file.write(f"BSSID: {data.bssid}\n")
                file.write(f"{data.ssid} Signal Strength: {data.signal}\n")
                file.write(f"Frequency: {data.freq} MHz\n")
                file.write("-" * 30 + "\n")
            break
   

def get_connected_wifi_ssid():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    print(f"Interface Name: {iface.name()}")
    iface.scan()
    scan_results = iface.scan_results()
    connected_ssid = iface.network_profiles()[0].ssid
    
    for network in scan_results:
        if network.ssid == connected_ssid and iface.status() == const.IFACE_CONNECTED:
            with open("wifi_nearby_stats.txt", "a") as file:
                file.write(f"Connected to: {network.ssid}\n")
                file.write(f"BSSID: {network.bssid}\n")
                file.write(f"{network.ssid} Signal Strength: {network.signal}\n")
                file.write(f"Frequency: {network.freq} MHz\n")
                file.write("-" * 30 + "\n")
            # print(f"Connected to: {network.ssid}")
            # print(f"BSSID: {network.bssid}")
            # print(f"Signal Strength: {network.signal} dbm")
            # print(f"Frequency: {network.freq} Mhz")
            # print("-" * 30)
            break
    else:
        print("No connected WiFi network found.")

if __name__ == "__main__":
    get_connected_wifi_ssid()
    get_nearby_wifi_stats()


        # Get the connected WiFi network
        # connected_ssid = iface.status() == const.IFACE_CONNECTED
        # connected_network = None
        # if iface.status() == const.IFACE_CONNECTED:
        #     connected_network = iface.network_profiles()[0].ssid
        #     print(f"connected to :{connected_network}")

        # if connected_network:
        #     print(f"SSID: {connected_network.ssid}")
        # else:
        #     print("Not connected to any WiFi network.")

        # print("\nNearby WiFi Networks:")
        # for network in scan_results:
        #     print(f"SSID: {network.ssid}")
        #     print(f"Signal Strength: {network.signal}")
        #     print(f"Frequency: {network.freq} MHz")
        #     print(f"Channel: {network.channel}")
        #     print(f"Encryption: {network.akm}")
        #     print("-" * 30)
        # print(f"Interface Name: {Name}")