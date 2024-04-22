import subprocess

interface = input("What interface are we replacing?")
mac

subprocess.call(f"ifconfig {interface} down", shell=True)
subprocess.call(f"ifconfig {interface} hw ether [macaddr]", shell=True)
subprocess.call(f"ifconfig {interface} up", shell=True)





