import subprocess

interface = input("What interface are we replacing?")
macaddr = input("What will be the new MAC address?")

subprocess.call(f"ifconfig {interface} down", shell=True)
subprocess.call(f"ifconfig {interface} hw ether {macaddr}", shell=True)
subprocess.call(f"ifconfig {interface} up", shell=True)

print(f"MAC address of {interface} has been changed to {macaddr}.")

verify_after = input("Verify interface after MAC address change (y/n)? ")
if verify_after.lower() == 'y':
    subprocess.call(f"ifconfig {interface}")
else:
    print("Verification skipped.")
