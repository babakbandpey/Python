#!/usr/bin/python3


import argparse

parser = argparse.ArgumentParser(description='Trying to scan an interface')

parser.add_argument('-p', help= 'port number', type = int, choices=range(0, 2 ** 16), default=80)

parser.add_argument('-ip', help= 'ip number', type = str)

parser.add_argument('-proto', help= '[tcp/ip]', type = str, choices=['tcp', 'udp'], default= 'tcp')



args = parser.parse_args()

print(args)
