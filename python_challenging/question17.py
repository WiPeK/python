#!/usr/bin/env python
# -*- coding: utf-8 -*-
res = 0
while True:
    line = input()
    if line:
        tmp = line.split(" ")
        if tmp[0] == "D":
        	res+=int(tmp[1])
        elif tmp[0] == "W":
        	res -= int(tmp[1])
    else:
        break
print (str(res))