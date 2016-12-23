#!/usr/bin/env python
# -*- coding: utf-8 -*-
#podzielne przez 5
inp = [x for x in input().split(",")]
res = []
for i in inp:
	if int(i, 2) % 5 == 0:
		res.append(str(i))

print (",".join(res))