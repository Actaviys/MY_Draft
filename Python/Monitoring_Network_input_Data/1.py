# pip install scapy

from scapy.all import sniff, IP, TCP, UDP, Raw
from datetime import datetime
from scapy.config import conf
from scapy.all import sniff, IP

def packet_callback(packet):
    if IP in packet:
        print(f"IP Packet: {packet.summary()}")
    # Отримуємо поточний час
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Перевіряємо, чи це IP-пакет
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto

        # Ідентифікуємо протокол
        if protocol == 6:  # TCP
            protocol_name = "TCP"
        elif protocol == 17:  # UDP
            protocol_name = "UDP"
        else:
            protocol_name = "Other"

        # Вхідний чи вихідний пакет
        direction = "Incoming" if packet[IP].dst == my_ip else "Outgoing"
        
        # Формуємо та друкуємо інформацію про пакет
        print(f"[{timestamp}] {direction} Packet:")
        print(f"  Protocol: {protocol_name}")
        print(f"  Source IP: {src_ip}")
        print(f"  Destination IP: {dst_ip}")

        # Якщо є корисні дані, додаємо їх
        if Raw in packet:
            data = packet[Raw].load.decode(errors="ignore")
            print(f"  Data: {data}")
        print("-" * 50)

# Отримуємо свою IP-адресу
import socket
my_ip = socket.gethostbyname(socket.gethostname())
conf.L3socket = True  # Переключення на рівень 3

# Запускаємо моніторинг
print(f"Monitoring packets on {my_ip}...")
sniff(filter=my_ip, prn=packet_callback, store=False)