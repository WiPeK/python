#!/usr/bin/env python
# -*- coding: utf-8 -*-
def compute(n):
	if n == 0:
		return 1
	else:
		return compute(n-1)+100

inp = int(input())
print(str(compute(inp)))