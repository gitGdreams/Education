import subprocess
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-i", "--interface", dest="interface", help="Interface to change its MAC address")
parser.add_argument("-m", "--macaddress", dest="macaddr", help="Replace MAC address")

args = parser.parse_args()

interface = args.interface
macaddr = args.macaddr

subprocess.call(f"ifconfig {interface} down", shell=True)
subprocess.call(f"ifconfig {interface} hw ether {macaddr}", shell=True)
subprocess.call(f"ifconfig {interface} up", shell=True)

print(f"MAC address of {interface} has been changed to {macaddr}.")
