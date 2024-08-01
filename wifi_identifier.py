import pywifi
from pywifi import const
import time


def get_nearby_wifi_stats(location):

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
        with open(f"{location}_wifi_nearby_stats.txt", "a", encoding='utf-8') as file:
            for data in scan_results:
                file.write(f"SSID: {data.ssid}\n")
                file.write(f"BSSID: {data.bssid}\n")
                file.write(f"{data.ssid} Signal Strength: {data.signal}\n")
                file.write(f"Frequency: {data.freq} MHz\n")
                file.write("-" * 30 + "\n")
            break
   


def get_connected_wifi_ssid(location, fname, folder_path):
    wifi = pywifi.PyWiFi()
    # iface = wifi.interfaces()[0]
    # iface.remove_all_network_profiles()
    iface = wifi.interfaces()[0]
    print(f"Interface Name: {iface.name()}")
    iface.scan()
    scan_results = iface.scan_results()
    connected_ssid = iface.network_profiles()[0].ssid
    for network in scan_results:
        if network.ssid == connected_ssid and iface.status() == const.IFACE_CONNECTED:
            with open(f"{folder_path}/{fname}", "a") as file:
                file.write(f"Location: {location}\n")
                file.write(f"Connected to: {network.ssid}\n")
                file.write(f"Connected to BSSID: {network.bssid}\n")
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
def get_connected_wifi_bssid_subbssid(location, fname, folder_path):
    wifi = pywifi.PyWiFi()
    # iface = wifi.interfaces()[0]
    # iface.remove_all_network_profiles()
    iface = wifi.interfaces()[0]
    iface.scan()
    scan_results = iface.scan_results()
    connected_ssid = iface.network_profiles()[0].ssid
    
    print("connected ssid", connected_ssid)
    for network in scan_results:
        if network.ssid == connected_ssid and iface.status() == const.IFACE_CONNECTED:
            with open(f"{folder_path}/{fname}", "a") as file:
                file.write(f"Location: {location}\n")
                file.write(f"Connected to: {network.ssid}\n")
                file.write(f"Connected to BSSID: {network.bssid}\n")
                file.write(f"{network.bssid} Signal Strength: {network.signal}\n")
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
    location_name = input("Enter the location name: ")
    connected_wifi_log = location_name + '_connected_wifi_stats.txt'
    sub_bssid_log = location_name + '_connected_sub_bssid_stats.txt'
    #specify folder path
    sub_bssid_log_folder_path = './log/connected_ssid_stats/sub_bssid'
    connected_ssid_folder_path = './log/connected_ssid_stats'

    get_connected_wifi_ssid(location_name, connected_wifi_log, connected_ssid_folder_path)
    get_connected_wifi_bssid_subbssid(location_name, sub_bssid_log, sub_bssid_log_folder_path)
    get_nearby_wifi_stats(location_name)


# def get_nearby_wifi_stats():
#     wifi = pywifi.PyWiFi()
#     iface = wifi.interfaces()[0]
#     scan_results = iface.scan_results()
#     print("\nNearby WiFi Networks:")
#     for network in scan_results:
#         print(f"SSID: {network.ssid}")
#         print(f"Signal Strength: {network.signal}")
#         print(f"Frequency: {network.freq} MHz")
#         print(f"Encryption: {network.akm}")
#         print("-" * 30)