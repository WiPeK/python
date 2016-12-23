#!/usr/bin/env python
# -*- coding: utf-8 -*-
lines = []
while True:
    line = input()
    if line:
        lines.append(line.upper())
    else:
        break
print ('\n'.join(lines))