#!/usr/bin/env python
# -*- coding: utf-8 -*-

inp = [x for x in input().split(",")]
inp = list(map(int, inp))
ar = [[0 for x in range(inp[1])] for y in range(inp[0])]
for i in range(0, inp[0]):
	for j in range(0, inp[1]):
		ar[i][j] = (i*j)

print (ar)