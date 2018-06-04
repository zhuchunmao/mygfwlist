#!/usr/bin/python
import netaddr
import urllib2
import sys
content = urllib2.urlopen('https://raw.githubusercontent.com/zhuchunmao/mygfwlist/master/gfwiplist.txt').readlines()
if not content:
    sys.exit(1)
blocks = []
for cidr in content:
    if cidr.startswith("#"):
        continue
    if not cidr.strip():
        continue
    blocks.append(netaddr.IPNetwork(cidr.strip()))
if len(blocks) == 0:
 sys.exit(1)
file = open('/root/gfwlist/router', 'w')
file.truncate()
for net in netaddr.cidr_merge(blocks):
 string = 'route ' + str(net.ip) + ' ' + str(net.netmask) + ' vpn_gateway\n'
 file.write(string)
file.close()
