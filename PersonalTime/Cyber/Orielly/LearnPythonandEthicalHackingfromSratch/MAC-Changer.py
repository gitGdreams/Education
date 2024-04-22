import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--macaddress", dest="macaddr", help="Replace MAC address")
    return parser.parse_args()

def change_mac(interface, macaddr):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", macaddr])
    subprocess.call(["ifconfig", interface, "up"])
    print(f"MAC address of {interface} has been changed to {macaddr}.")
    subprocess.call(["ifconfig", interface])

(options, arguments) = get_arguments()
change_mac(options.interface, options.macaddr)
