import subprocess


subprocess.call("ifconfig wlan0 down", shell=True)
subprocess.call("ifconfig wlan0 hw ether [macaddr]", shell=True)
subprocess.call("ifconfig wlan0 up", shell=True)
