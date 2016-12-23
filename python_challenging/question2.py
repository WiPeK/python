#!/usr/bin/env python
# -*- coding: utf-8 -*-
def factorial(n):
	if n == 1 or n == 0:
		return 1
	else:
		return (n*factorial(n-1))

n = int(input())
print (factorial(n))