#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Strings:
	def __init__ (self):
		self.val = "testowy"

	def getString(self):
		self.val = input()

	def printString(self):
		print (self.val.upper())

o = Strings()
o.printString()
o.getString()
o.printString()