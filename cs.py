# -*- coding: utf-8 -*-
import re, platform

thisSys = platform.system()

s = '正在 Ping 3g.gzch120.com [101.37.22.146] 具有 32 字节的数据:'

# 将正则表达式编译成Pattern对象

if ('Windows' == thisSys):
    p = re.compile(r'.*\[(.*?)\]')
    match = p.split(s)
    if match and match[1]:
        print match[1]


