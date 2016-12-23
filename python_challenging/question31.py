#!/usr/bin/env python
# -*- coding: utf-8 -*-
def count(n):
	res = 0.0
	for i in range(1,n+1):
		res += i/(i+1)
	return res

inp = int(input())
print(str(round(count(inp),2)))
