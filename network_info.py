import socket
import psutil
from termcolor import colored

# Get the hostname of the computer
hostname = socket.gethostname()

# Get the IP addresses associated with the computer
ip_addresses = socket.gethostbyname_ex(hostname)[2]

# Get network interfaces and their configurations
network_interfaces = psutil.net_if_addrs()

# Define text colors
white = 'white'
blue = 'blue'
yellow = 'yellow'
green = 'green'

# Print the hostname and IP addresses in colored text
print(colored('Hostname:', blue), colored(hostname, white))
print(colored('IP Addresses:', blue))
for ip in ip_addresses:
    print(colored(ip, white))

# Print network interface configurations in colored text
print(colored('Network Interface Configurations:', blue))
for interface, addresses in network_interfaces.items():
    interface_name = interface.split(":")[1] if ":" in interface else interface
    print(colored('Interface:', blue), colored(interface_name, yellow))
    for address in addresses:
        if address.family == socket.AF_INET:
            print(colored('Address (IPv4):', blue), colored(address.address, green))
            print(colored('Netmask:', blue), colored(address.netmask, white))
            print(colored('Broadcast Address:', blue), colored(address.broadcast, white))
        elif address.family == socket.AF_INET6:
            print(colored('Address (IPv6):', blue), colored(address.address, white))
            print(colored('Netmask:', blue), colored(address.netmask, white))
        elif address.family == psutil.AF_LINK:
            print(colored('MAC Address:', blue), colored(address.address, white))
    print()
