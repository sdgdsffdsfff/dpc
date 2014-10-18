#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
from nginxParse import nginxParse
from datetime import datetime

dpc_file = 'input/dpc.txt'
nginx_file = 'input/nginx.txt'
output_file = 'output/LogSuccess.txt'

success_dict = {}
result_list = []


def generateDpcKey(nginxDict):
    dpc_time = nginxDict['log_time'].strftime("%Y%m%d%H%M")
    user_agent = nginxDict['user_agent'].replace(" ","").lower()
    key = '-'.join([dpc_time, user_agent])
    return key

def parseTime(time_str):
    time_obj = datetime.strptime(time_str, "%Y%m%d%H%M")
    return time_obj.strftime("%Y-%m-%d %H:%M")

def processNginx():
    nginx_obj = nginxParse()
    i = 1
    with open(nginx_file, encoding="utf-8") as f:
        for line in f:
            line = line.strip("\n")
            print("\rProcess Nginx: {0}".format(i), end="")
            i += 1

            nginx_dict = nginx_obj.process(line)
            key = generateDpcKey(nginx_dict)

            if key in success_dict:
                success_dict[key] += 1
            else:
                success_dict[key] = 1

    print("")

def processDPC():
    i = 1
    with open(dpc_file, encoding="utf-8") as f:
        for line in f:
            print("\rProcess DPC: {0}".format(i), end="")
            i += 1

            line = line.strip('\n')
            line_arr = line.split('\t')

            record_dict = {
                'ip' : line_arr[1],
                'time' : parseTime(line_arr[0]),
                'user_agent' : line_arr[2],
                'dst_url' : line_arr[3],
                'success' : False
            }

            user_agent = line_arr[2].replace(' ','')
            key = '-'.join([line_arr[0], user_agent.lower()])

            if key in success_dict:
                if success_dict[key] > 0:
                    success_dict[key] -= 1
                record_dict['success'] = True

            result_list.append(record_dict)


def writeFile():
    write_str = ""
    failed_str = ""

    for item in result_list:
        record_str = ""
        record_str = '\t'.join([item['time'], item['ip'], item['dst_url'], item['user_agent']])

        if item['success']:
            record_str = "Success\t" + record_str
        else:
            record_str = " \t" + record_str

        write_str += record_str + "\n"

    for item in success_dict:
        if success_dict[item] > 0:
            failed_record = item.split('-')
            user_agent = '-'.join(failed_record[1:])
            failed_str += '\t'.join([' ', parseTime(failed_record[0]), ' ', ' ', user_agent]) + "\n"

    if failed_str:
        write_str += "\n\nSuccess Not Match\n\n"
        write_str += failed_str

    with open(output_file,"w+") as f:
        f.write(write_str)
        print("\nWirte file done")


if __name__ == '__main__':
    processNginx()
    processDPC()
    writeFile()