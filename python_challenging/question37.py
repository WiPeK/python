#!/usr/bin/env python
# -*- coding: utf-8 -*-
import zlib

t = 'hello world!hello world!hello world!hello world!'
print (t)
print (len(t))
zlib.compress(t)
print (len(t))
print(str(t))
zlib.decompress(t)
print (len(t))
print(str(t))