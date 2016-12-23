#!/usr/bin/env python
# -*- coding: utf-8 -*-
bar = {}
inp = input()
for i in inp.split():
	bar[i] = bar.get(i,0)+1

a = bar.keys()
a = sorted(a)

for i in a:
	print(i + ":" + str(bar[i]))