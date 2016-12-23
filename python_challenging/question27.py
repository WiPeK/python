#!/usr/bin/env python
# -*- coding: utf-8 -*-
li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = filter(lambda x: x&1, li)
print (evenNumbers)

li = [1,2,3,4,5,6,7,8,9,10]
squaredNumbers = map(lambda x: x**2, li)
print (squaredNumbers)