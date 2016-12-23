#!/usr/bin/env python
# -*- coding: utf-8 -*-
l = []
for i in range(1000, 3001):
	s = str(i)
	if not(int(s[0])&1) and not(int(s[1])&1) and not(int(s[2])&1) and not(int(s[3])&1):
		l.append(str(i))

print(",".join(l))