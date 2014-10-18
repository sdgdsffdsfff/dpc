#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from ipCompare import ipCompare
import logging
from ipaddress import IPv4Network

dpc_file = 'input/dpc.txt'
nginx_file = 'input/nginx.txt'
output_file = 'output/IpRate.txt'
ipObj = ipCompare()

ip_pool = {}


def processDPC(ip_addr):

    ip_net = ipObj.parsePrivateIP(ip_addr)

    if ip_net is None:
        logging.error("ERROR: process ip {0} error".format(ip_addr))
        return

    if ip_net in ip_pool:
        ip_pool[ip_net]['total'] += 1
    else:
        item = {'total' : 1, 'success' : 0}
        ip_pool[ip_net] = item

def processNginx(ip_addr):

    ip_net = ipObj.transPublicIP(ip_addr)

    if ip_net is None:
        try:
            ip_net = ip_addr + '/24'
            ip_net = IPv4Network(ip_net, False)
        except:
            logging.error("Error: error to handle ip {0}".format(ip_addr))
            return


    if ip_net in ip_pool:
        ip_pool[ip_net]['success'] += 1
    else:
        item = {'total' : 0, 'success' : 1}
        ip_pool[ip_net] = item

def writePoolFile():
    file_str = ""

    for item in ip_pool:
        file_str += "{0}\t{1}\t{2}\n".format(str(item), ip_pool[item]['success'], ip_pool[item]['total'])

    with open(output_file, 'w+') as f:
        f.write(file_str)

    print("write pool file done")


def main():
    i = 1
    with open(dpc_file, encoding="utf-8") as f:
        for line in f:
            line = line.strip('\n')
            ip_addr = line.split('\t')[1]
            print("\r Process DPC: {0} IP: {1}".format(i, ip_addr), end="")
            processDPC(ip_addr)
            i += 1

    print("\n")
    i = 1

    with open(nginx_file, encoding="utf-8") as f:
        for line in f:
            line = line.strip('\n')
            ip_addr = line.split(' ')[0]
            print("\r Process Nginx: {0} IP: {1}".format(i, ip_addr), end="")
            processNginx(ip_addr)
            i += 1

    print("\n")

    writePoolFile()


if __name__ == '__main__':
    main()

