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
total_dpc_line = 0
total_nginx_line = 0


def processDPC(ip_addr):
    global ip_pool

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
    global ip_pool

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

def generatePoolReuslt():
    file_str = ""
    print_str = ""
    global ip_pool, total_dpc_line, total_nginx_line

    for item in ip_pool:
        success_num = ip_pool[item]['success']
        total_num = ip_pool[item]['total']
        if total_num != 0 and success_num != 0:
            ratio = round(success_num / total_num *100, 1)
            ratio = str(ratio) + "%"
        else:
            ratio = "0"

        # Generate file str
        file_str += "{0}\t{1}\t{2}\t{3}\n".format(str(item), success_num, total_num, ratio)

        # Generate print str
        if success_num >= 5 or total_num >=5:
            print_str += "%20s %8s %8s %8s\n" % (str(item),success_num, total_num, ratio)

    print("----------------")
    print("total: {0}\tsuccess: {1}\tratio: {2}%".
          format(total_dpc_line,total_nginx_line,round(total_nginx_line/total_dpc_line*100,1)))
    print("----------------")
    print(print_str)
    print("----------------")

    with open(output_file, 'w+') as f:
        f.write(file_str)

    print("write pool file done")


def main():
    global total_dpc_line, total_nginx_line

    with open(dpc_file, encoding="utf-8", errors='ignore') as f:
        for line in f:
            total_dpc_line += 1
            line = line.strip('\n')
            ip_addr = line.split('\t')[1]
            print("\r Process DPC: {0} IP: {1}".format(total_dpc_line, ip_addr), end="")
            processDPC(ip_addr)

    print("\n")

    with open(nginx_file, encoding="utf-8", errors='ignore') as f:
        for line in f:
            total_nginx_line += 1
            line = line.strip('\n')
            ip_addr = line.split(' ')[0]
            print("\r Process Nginx: {0} IP: {1}".format(total_nginx_line, ip_addr), end="")
            processNginx(ip_addr)

    print("\n")

    generatePoolReuslt()


if __name__ == '__main__':
    main()

