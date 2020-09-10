#MAC Changer
A system MAC address changing program until unless a reversal/ a complete system boot is initiated.

## Modules involved
* subprocess
* optparse
* re

## functions created in the program
* get_arguments()
To parse the system input data and separate it into corresponding fields along with impromptu message display
* get_current_mac(interface)
To obtain the current mac address of the system to change it into the corresponding input mac address.
* change_mac(interface, new_mac)
changing the mac address in a hard-coded way in the terminal with subprocess module's help.