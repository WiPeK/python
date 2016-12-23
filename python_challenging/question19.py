#!/usr/bin/env python
# -*- coding: utf-8 -*-
from operator import itemgetter, attrgetter
lines = []
while True:
    line = input()
    if line:
        lines.append(tuple(line.split(",")))
    else:
        break

print (sorted(lines, key=itemgetter(0,1,2)))