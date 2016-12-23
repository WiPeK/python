#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Divisible:
	n = 0
	def __init__(self,n):
		self.n = n

	def generate(self):
		for i in range(0, self.n):
			if i%7 == 0:
				yield i

n = int(input())
o = Divisible(n)
for i in o.generate():
	print (i)