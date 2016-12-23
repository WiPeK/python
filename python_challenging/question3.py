#!/usr/bin/env python
# -*- coding: utf-8 -*-
def create_dict(n):
	d = dict()
	for i in range(1, n+1):
		d[i] = i*i
	return d

n = int(input())
print (create_dict(n))