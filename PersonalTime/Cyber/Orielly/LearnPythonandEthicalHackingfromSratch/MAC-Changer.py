import subprocess
import argparse

parser = argparse.OptionParser()

parser.add_option("-i", "--interface", dest ="interface", help="Interface to change its MAC address")
parser.add_option("-m", "--mac address", dest = "macaddr", help = "Replace MAC")

(options, arguments) = parser.parse_args()

interface = options.interface
macaddr = options.macaddr

subprocess.call(f"ifconfig {interface} down", shell=True)
subprocess.call(f"ifconfig {interface} hw ether {macaddr}", shell=True)
subprocess.call(f"ifconfig {interface} up", shell=True)

print(f"MAC address of {interface} has been changed to {macaddr}.")


