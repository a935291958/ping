# -*- coding: utf-8 -*-
import os, sys,platform
from common import *

# url文件
urlFile = "url.txt"
# 成功的网站保存地址
succFileName = './res/success.txt'
# 失败的网站保存地址
failFileName = './res/fail.txt'

# 成功ping通的列表
succLsit = ''
# ping不同的列表
failList = ''

# 计数，ping成功的网站
succCount = 0

# 计数，ping失败的网站
failCount = 0

if not isFile(urlFile):
    msg('File does not exist', 4)
    sys.exit(0)

# 打开文件
fo = open(urlFile, "r")
msg('file name is %s' % (urlFile), 1)

for line in fo.readlines():  # 依次读取每行
    line = line.strip()  # 去掉每行头尾空白
    line = line.replace('\n', '')  # 去掉每行换行符
    # 空行的话跳过
    if (not line):
        continue

    msg("The current link %s " % (line), 1)
    # 执行ping 命令
    res = os.popen('ping -n 1 ' + line)
    # 读取返回值 并全部转换为大写
    resStr = res.read().upper()
    # print res
    # if ('TTL' not in resStr):
    # res = os.system('ping -n 1 ' + line)

    # print res
    # 判断有没有ping通
    # if (res == 1):
    if ('TTL' not in resStr):
        failList += line + '\n'
        msg("The visit to fail %s" % (line), 2)
        failCount += 1
    else:
        #获取IP
        ip = ''
        thisSys = platform.system()
        if ('Windows' == thisSys):
            p = re.compile(r'.*\[(.*?)\]')
            match = p.split(resStr)
            if match and match[1]:
                ip =  match[1]
        succLsit += line + ' '+ip + '\n'

        msg("Successful visit %s" % (line), 1)
        succCount += 1
# 关闭文件
fo.close()

# 把结果写入文件
failFile = open(failFileName, 'w')
failFile.write(failList)
failFile.close()

succFile = open(succFileName, 'w')
succFile.write(succLsit)
succFile.close()

msg('The number of successful:' + str(succCount), 1)
msg('The total number of failures:' + str(failCount), 1)
