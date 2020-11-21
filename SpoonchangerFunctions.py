#!usr/bin/env python

import subprocess
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address to potato")
    parser.add_option("-m", "--mac", dest="new_mac", help="New potato MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error(" You are potato, enter interface name, use --help for happiness ")
    elif not options.new_mac:
        parser.error(" You are potato, enter new MAC address, use --help for happiness ")
    return options

def change_mac(interface, new_mac):
    print("Changing MAC address for " + interface + " to " +new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


options = get_arguments()
change_mac(options.interface, options.new_mac)

ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
print(ifconfig_result)

