#!/usr/bin/env python
import subprocess
import optparse
import re

#Function to get user arguments
def get_Arguments():
    parser=optparse.OptionParser()
    parser.add_option("-i","--interface",dest="interface",help="interface To Change Mac Adress")
    parser.add_option("-m","--mac",dest="new_mac",help="New Mac Adress")
    (options,arguments)=parser.parse_args()
    if not options.interface:
        parser.error("[+] Please Specify Interface Or use --help for more Info." )
    if not options.new_mac:
        parser.error("[+] Please Specify a New MAC  Or use --help for more Info." )
    return options

#function for changing mac adress
def change_Mac(interface,new_mac):
    print("[+] Changing Mac adress for " + interface + " to "+ new_mac)
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
    subprocess.call(["ifconfig",interface,"up"])

#function for getting current mac
def get_Current_mac(interface):
    ifconfig_result=subprocess.check_output(["ifconfig",interface])
    mac_address_search=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig_result)
    if mac_address_search:
        return mac_address_search.group(0)
    else:
        print("[+] Could not Read Mac Adress")

options=get_Arguments()
current_mac=get_Current_mac(options.interface)
print("[+] Current Mac "+str(current_mac))
change_Mac(options.interface,options.new_mac)
current_mac=get_Current_mac(options.interface)
if current_mac==options.new_mac:
    print("[+] Mac Address was Sucessfully Changed To "+ current_mac)
else:
    print("[-] Can't Change Mac Adress")
