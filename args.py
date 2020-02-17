#!/usr/bin/python3


import argparse

import ipaddress

parser = argparse.ArgumentParser(description='Trying to scan an interface')

parser.add_argument('-p', help= 'port number', type = int, choices=range(0, 2 ** 16), default=80)

parser.add_argument('-ip', help= 'ip number', type = str)

parser.add_argument('-proto', help= '[tcp/ip]', type = str, choices=['tcp', 'udp'], default= 'tcp')



args = parser.parse_args()

print(args)


try:
	ip_addr = ipaddress.ip_address(args.ip)
except ValueError:
	print("Bad IP number: {0}".format(args.ip))
	# handle bad ip
