import subprocess

interface = input("What interface are we replacing?")
macaddr = input("What will be the new MAC address?")

subprocess.call(f"ifconfig {interface} down", shell=True)
subprocess.call(f"ifconfig {interface} hw ether {macaddr}", shell=True)
subprocess.call(f"ifconfig {interface} up", shell=True)





