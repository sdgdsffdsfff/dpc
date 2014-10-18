#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
from datetime import datetime

class nginxParse:
    def __init__(self):
        pass

    def process(self, record):
        res_line = self.parse_line(record)
        return self.parse_nginx_format(res_line)

    def parse_line(self, line):
        pat = (r''
               '(\d+.\d+.\d+.\d+)\s-\s-\s' #IP address
               '\[(.+)\]\s' #datetime
               '"GET\s(.+)\s\w+/.+"\s\d+\s' #requested file
               '\d+\s"(.+)"\s' #referrer
               '"(.+)"' #user agent
            )
        match = re.findall(pat, line)
        if match:
            return match
        else:
            return None

    def parse_nginx_format(self, nginx_array):
        if nginx_array is None:
            return None

        nginx_dict = {}

        nginx_array = nginx_array[0]
        nginx_dict['ip_addr'] = nginx_array[0]
        nginx_dict['log_time'] = self.process_nginx_time(nginx_array[1])
        nginx_dict['dst_url'] = nginx_array[2]
        nginx_dict['reference'] = nginx_array[3]
        nginx_dict['user_agent'] = nginx_array[4]

        return nginx_dict

    def process_nginx_time(self, time_str):
        date_str = time_str.split(" ")[0]
        date_obj = datetime.strptime(date_str, "%d/%b/%Y:%H:%M:%S")
        return date_obj

def test():
    nginx_obj = nginxParse()
    with open('input/nginx.txt', 'r') as f:
        for line in f:
            line = line.strip("\n")
            print(nginx_obj.process(line))

if __name__ == '__main__':
    test()