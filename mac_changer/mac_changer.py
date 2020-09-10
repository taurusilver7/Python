#!usr/env/bin/python

import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option('-i', '--interface', dest='interface', help=' Enter interface name')
    parser.add_option('-m', '-mac', dest='new_mac', help='new MAC address')
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error('[-] Please specify a interface name or use --help option')
    elif not options.new_mac:
        parser.error('[-] Please specify a MAC address or use --help option')
    return options

def change_mac(interface, new_mac):
    print('Changing the MAC address of interface ' + interface + ' to ' + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    result = subprocess.check_output(["ifconfig", interface])
    mac_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(result))
    if mac_result:
        return mac_result.group(0)   # first result obtained from filter re.    
    else:
        print('[-]Could not read MAC address')

options = get_arguments()
current_mac = get_current_mac(options.iinterface)

print("Current MAC: " + str(current_mac))

change_mac(options.interface, options.new_mac)

if current_mac == options.new_mac:
    print("[-]MAC address was successfully changed to " + str(current_mac))
else:
    print("[-]MAC address did not get changed")
