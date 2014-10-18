#!/bin/bash

DPC_FOLDER=$1

for dpc_file in ${DPC_FOLDER}/mtdpc_redirect_*; do
	temp_file=`basename $dpc_file`
	echo "analyse $temp_file"
	time_file=`echo $temp_file | awk -F '_' '{print $3}'`
	time=`echo $time_file | awk -F '.' '{print $1}' `
	grep "playniuniu" $dpc_file | grep "www\.baidu\.com" | awk -F '\1' '{printf("%s\t%s\t%s\t%s\n", "'$time'",$10,$12,$9)}' >> result.txt
done
