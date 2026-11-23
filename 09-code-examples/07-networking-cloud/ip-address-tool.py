"""IP Address Information Tool — Kilele TechPath, Pathway 7 (Networking & Cloud).

Introduces IP addresses and subnet information.
Run with: python3 ip-address-tool.py
"""

import ipaddress


def analyze_network(address):
    try:
        network = ipaddress.ip_network(address, strict=False)

        print("\nNETWORK INFORMATION")
        print("-------------------")

        print("Network Address:", network.network_address)
        print("Broadcast Address:", network.broadcast_address)
        print("Subnet Mask:", network.netmask)
        print("Number of Addresses:", network.num_addresses)

        if network.version == 4:
            print("IP Version: IPv4")
        else:
            print("IP Version: IPv6")

    except ValueError:
        print("Invalid IP address or network range.")


def main():
    user_address = input("Enter an IP address or CIDR range: ")
    analyze_network(user_address)


if __name__ == "__main__":
    main()
