#!/usr/bin/env python
# -*- coding: utf-8 -*-
inp = input()
res = 0
for i in range(1, 5):
	s = inp
	for j in range(1,i):
		s+=inp
	res += int(s)

print(str(res))