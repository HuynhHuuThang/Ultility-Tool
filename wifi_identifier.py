import pywifi
from pywifi import const
import time
import logging

def remove_all_profiles(iface):
    profiles = iface.network_profiles()
    for profile in profiles:
        iface.remove_network_profile(profile)

def get_wifi_stats():

    start_time = time.time()
    duration=60

    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    while time.time() - start_time < duration:
        iface.scan()
        scan_results = iface.scan_results()
        for data in scan_results:
            print(f"SSID: {data.ssid}")
            print(f"BSSID: {data.bssid}")
            print(f"{data.ssid} Signal Strength: {data.signal}")
            print(f"Frequency: {data.freq} MHz")
    print("\n" + "=" * 50 + "\n")
    # Wait for 5 seconds before the next scan
    time.sleep(5)  

def get_connected_wifi_ssid():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    print(f"Interface Name: {iface.name()}")
    iface.scan()
    scan_results = iface.scan_results()
    connected_ssid = iface.network_profiles()[0].ssid
    
    for network in scan_results:
        if network.ssid == connected_ssid and iface.status() == const.IFACE_CONNECTED:
            print(f"Connected to: {network.ssid}")
            print(f"Signal Strength: {network.signal} dbm")
            print(f"Frequency: {network.freq} Mhz")
            print("-" * 30)
            break
    else:
        print("No connected WiFi network found.")

if __name__ == "__main__":
    get_connected_wifi_ssid()


    # get_wifi_stats()


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