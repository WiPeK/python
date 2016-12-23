#!/usr/bin/env python
# -*- coding: utf-8 -*-
inp = input()
let = 0
num = 0
for i in inp:
	if i.isdigit():
		num = num+1
	elif i.isalpha():
		let = let + 1

print ("LETTERS " + str(let))
print ("DIGITS " + str(num))
