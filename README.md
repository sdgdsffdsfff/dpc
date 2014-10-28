# DPC 日志分析

#### 分析百川的DPC日志数据

###### 1. 提取 Nginx 日志

提取 nginx 上的访问日志，由于百川的 DPC 有两种方式，redirect 和 ad.0.js， 所以需要使用 grep 针对不同网站的两种模式做提取。

以 jd.com 为例，分析10月24日的日志数据，grep的代码入下：

* redirect 脚本：


`grep '24\/Oct\/' log/access.log | grep -v 'ad\.0\.js' | grep 'jd\.com' > nginx.txt`


* ad.0.js 脚本：


`grep '24\/Oct' log/access.log | grep 'ad\.0\.js' | grep 'jd\.com' > nginx.txt`


###### 2. 提取百川日志

利用 dpcsh 文件夹中得 Shell 脚本，提取百川程序的日志，根据不同的模式，脚本也分为两种，提取 redirect 的脚本和提取 js 的脚本

* redirect 脚本：

`./dpc.sh /var/log/dpc/20141024 redirect`

* ad.0.js 脚本：

`./dpc.sh /var/log/dpc/20141024 js`

该脚本最终会在当前文件夹产生一个 dpc.txt 文件


###### 3. 分析日志

1. 在根目录新建 input 和 output 文件夹

2. 将步奏 1 和 2 中产生的 dpc.txt 和 nginx.txt 放入 input 文件夹

3. 运行 analysisIpRange.py 即可查看结果 

