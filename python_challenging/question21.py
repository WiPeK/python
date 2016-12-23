#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

class Distance:
	startX = 0
	startY = 0
	endX = 0
	endY = 0
	res = 0
	def changeX(self, x):
		self.endX = x

	def changeY(self, y):
		self.endY = y

	def countDistance(self):
		self.res = int(round(math.sqrt(( self.startX - self.endX )**2 + ( self.startY - self.endY )**2 )))

lines = []
while True:
    line = input()
    if line:
        lines.append(tuple(line.split(" ")))
    else:
        break

o = Distance()
for i in lines:
	if i[0] == "UP":
		o.changeY(o.endY + int(i[1]))
	elif i[0] == "DOWN":
		o.changeY(o.endY - int(i[1]))
	elif i[0] == "LEFT":
		o.changeX(o.endX - int(i[1]))
	elif i[0] == "RIGHT":
		o.changeX(o.endX + int(i[1]))

print (o.endX)
print (o.endY)
o.countDistance()
print (o.res)