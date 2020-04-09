#!/usr/bin/env python

import scapy.all as scapy
import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help= "Target IP addr/ IP range")
    options = parser.parse_args()
    return options

def scan(ip):
    arp_req = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_packet = broadcast/arp_req
    ans = scapy.srp(arp_packet, timeout=1, verbose=False)[0]

    list = []
    for element in ans:
        dict = {"IP": element[1].psrc, "MAC": element[1].hwsrc}
        list.append(dict)
    return list

def print_result(result):
    print(" IP\t\t\t  MAC Address\n-------------------------------------------")
    for client in result:
        print(client["IP"] + "\t\t" + client["MAC"])

options = get_arguments()
scan_result = scan(options.target)
print_result(scan_result)