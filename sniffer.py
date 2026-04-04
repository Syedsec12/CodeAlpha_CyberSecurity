from scapy.all import *

def packet_callback(packet):
    print("\n--- New Packet ---")

    if packet.haslayer(IP):
        ip_layer = packet[IP]
        print(f"Source IP: {ip_layer.src}")
        print(f"Destination IP: {ip_layer.dst}")

    if packet.haslayer(TCP):
        print("Protocol: TCP")
    elif packet.haslayer(UDP):
        print("Protocol: UDP")
    else:
        print("Protocol: Other")

# Start sniffing
sniff(prn=packet_callback, count=10)