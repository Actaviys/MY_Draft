from scapy.all import sniff, IP

def packet_callback(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        print(f"Packet: {src_ip} -> {dst_ip}")

# Використання рівня 3
sniff(filter="ip", prn=packet_callback, store=False)