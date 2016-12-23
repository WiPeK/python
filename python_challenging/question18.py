#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
inp = input()
inp = inp.split(",")
isLowerAlpha = 0
isNumber = 0
isUpperAlpha = 0
isChar = 0
okLen = 0

res = []

for i in inp:
	if re.search("[a-z]", i):
		isLowerAlpha = 1
	if re.search("[0-9]", i):
		isNumber = 1
	if re.search("[A-Z]", i):
		isUpperAlpha = 1
	if re.search("[$#@]", i):
		isChar = 1
	if len(i) >= 6 and len(i) <= 12:
		okLen = 1

	if isLowerAlpha and isNumber and isUpperAlpha and isChar and okLen:
		res.append(i)

print(",".join(res))

