#!/usr/bin/env python
# -*- coding: utf-8 -*-
inp = input()
up = 0
low = 0
for i in inp:
	if i.isupper():
		up += 1
	elif i.islower():
		low += 1

print ("UPPER " + str(up))
print ("LOWER " + str(low))
