#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from ipaddress import IPv4Network, IPv4Address
import logging

ip_manyou_106 = IPv4Network('106.33.0.0/16', False)
ip_manyou_171 = IPv4Network('171.9.0.0/16', False)
ip_wap_gw = IPv4Network('222.85.88.145/32', False)

ip_net_240 = IPv4Network('106.46.240.0/24', False)
ip_net_241 = IPv4Network('106.46.241.0/24', False)
ip_net_242 = IPv4Network('106.46.242.0/24', False)
ip_net_243 = IPv4Network('106.46.243.0/24', False)
ip_net_244 = IPv4Network('106.46.244.0/24', False)
ip_net_245 = IPv4Network('106.46.245.0/24', False)
ip_net_246 = IPv4Network('106.46.246.0/24', False)
ip_net_247 = IPv4Network('106.46.247.0/24', False)

ip_wap_240 = IPv4Network('123.101.240.0/24', False)
ip_wap_241 = IPv4Network('123.101.241.0/24', False)
ip_wap_242 = IPv4Network('123.101.242.0/24', False)
ip_wap_243 = IPv4Network('123.101.243.0/24', False)
ip_wap_244 = IPv4Network('123.101.244.0/24', False)
ip_wap_245 = IPv4Network('123.101.245.0/24', False)
ip_wap_246 = IPv4Network('123.101.246.0/24', False)
ip_wap_247 = IPv4Network('123.101.247.0/24', False)

ip_wap_250 = IPv4Network('123.101.250.0/24', False)
ip_wap_251 = IPv4Network('123.101.251.0/24', False)


ip_wap_253_1 = IPv4Network('123.101.253.0/26', False)
ip_wap_253_2 = IPv4Network('123.101.253.64/26', False)
ip_wap_253_3 = IPv4Network('123.101.253.128/26', False)
ip_wap_253_4 = IPv4Network('123.101.253.196/26', False)
ip_wap_254_1 = IPv4Network('123.101.254.0/26', False)
ip_wap_254_2 = IPv4Network('123.101.254.64/26', False)

ip_net_34 = IPv4Network('10.34.0.0/16', False)
ip_net_35 = IPv4Network('10.35.0.0/16', False)
ip_net_36 = IPv4Network('10.36.0.0/16', False)
ip_net_37 = IPv4Network('10.37.0.0/16', False)
ip_net_38 = IPv4Network('10.38.0.0/16', False)
ip_net_39 = IPv4Network('10.39.0.0/16', False)
ip_net_40 = IPv4Network('10.40.0.0/16', False)
ip_net_41 = IPv4Network('10.41.0.0/16', False)

ip_wap_42 = IPv4Network('10.42.0.0/16', False)
ip_wap_43 = IPv4Network('10.43.0.0/16', False)
ip_wap_44 = IPv4Network('10.44.0.0/16', False)
ip_wap_45 = IPv4Network('10.45.0.0/16', False)
ip_wap_46 = IPv4Network('10.46.0.0/16', False)
ip_wap_47 = IPv4Network('10.47.0.0/16', False)
ip_wap_48 = IPv4Network('10.48.0.0/16', False)
ip_wap_49 = IPv4Network('10.49.0.0/16', False)
ip_wap_50 = IPv4Network('10.50.0.0/16', False)
ip_wap_51 = IPv4Network('10.51.0.0/16', False)
ip_wap_52 = IPv4Network('10.52.0.0/16', False)
ip_wap_53 = IPv4Network('10.53.0.0/16', False)
ip_wap_68 = IPv4Network('10.68.0.0/16', False)
ip_wap_69 = IPv4Network('10.69.0.0/16', False)
ip_wap_70 = IPv4Network('10.70.0.0/16', False)
ip_wap_71 = IPv4Network('10.71.0.0/16', False)
ip_wap_72 = IPv4Network('10.72.0.0/16', False)
ip_wap_73 = IPv4Network('10.73.0.0/16', False)


reverse_nat_table = {
    ip_manyou_106 : ip_manyou_106,
    ip_manyou_171 : ip_manyou_171,
    ip_wap_gw  : ip_wap_gw,
    ip_net_240 : ip_net_34,
    ip_net_241 : ip_net_35,
    ip_net_242 : ip_net_36,
    ip_net_243 : ip_net_37,
    ip_net_244 : ip_net_38,
    ip_net_245 : ip_net_39,
    ip_net_246 : ip_net_40,
    ip_net_247 : ip_net_41,
    ip_wap_240 : ip_wap_48,
    ip_wap_241 : ip_wap_49,
    ip_wap_242 : ip_wap_50,
    ip_wap_243 : ip_wap_51,
    ip_wap_244 : ip_wap_52,
    ip_wap_245 : ip_wap_53,
    ip_wap_246 : ip_wap_42,
    ip_wap_247 : ip_wap_43,
    ip_wap_250 : ip_wap_46,
    ip_wap_251 : ip_wap_47,
    ip_wap_253_1 : ip_wap_68,
    ip_wap_253_2 : ip_wap_69,
    ip_wap_253_3 : ip_wap_70,
    ip_wap_253_4 : ip_wap_71,
    ip_wap_254_1 : ip_wap_72,
    ip_wap_254_2 : ip_wap_73,
}

ip_public_list = [
    ip_manyou_106,
    ip_manyou_171,
    ip_wap_gw ,
    ip_net_240,
    ip_net_241,
    ip_net_242,
    ip_net_243,
    ip_net_244,
    ip_net_245,
    ip_net_246,
    ip_net_247,
    ip_wap_240,
    ip_wap_241,
    ip_wap_242,
    ip_wap_243,
    ip_wap_244,
    ip_wap_245,
    ip_wap_246,
    ip_wap_247,
    ip_wap_250,
    ip_wap_251,
]


class ipCompare:
    def __init__(self):
        pass

    def transPublicIP(self, ip_public):
        try:
            ip_addr = IPv4Address(ip_public)

            ip_public_net = None

            for item in ip_public_list:
                if ip_addr in item:
                    ip_public_net = item
                    break

            if ip_public_net:
                if ip_public_net in reverse_nat_table:
                    return reverse_nat_table[ip_public_net]
                else:
                    logging.debug("IP address {0} not in nat table".format(ip_public))
            else:
                logging.debug("Not find for ip {0}".format(ip_public))
                return None

        except:
            logging.error("ERROR: not ipv4 format")
            return None

    def parsePrivateIP(self, ip_private):
        """

        :rtype : object
        """
        try:
            ip_private_net = ip_private + '/16'
            ip_private_net = IPv4Network(ip_private_net, False)
            return ip_private_net
        except:
            print("1")
            logging.error("ERROR: not ipv4 format")
            return None


def test():
    ipObj = ipCompare()
    print(ipObj.transPublicIP('106.46.241.3'))
    print(ipObj.transPublicIP('171.9.241.3'))
    print(ipObj.parsePrivateIP('10.34.232.5'))
    print(ipObj.parsePrivateIP('106.33.232.5'))

if __name__ == '__main__':
    test()