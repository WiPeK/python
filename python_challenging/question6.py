#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
class Count:
	C = 0
	H = 0
	D = []
	roots = []
	def __init__ (self, D):
		self.C = 50
		self.H = 30
		self.D = list(map(int, D))

	def countSquare(self):
		for i in range(0, len(self.D)):
			self.roots.append(str(round(math.sqrt((2 * self.C * self.D[i]) / self.H))))


print ("Podaj D")
i = input()
n = i.split(",")
c = Count(n)
c.countSquare()
print (",".join(c.roots))


