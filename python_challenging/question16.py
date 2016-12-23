#!/usr/bin/env python
# -*- coding: utf-8 -*-
values = input()
numbers = [x for x in values.split(",") if int(x)&1]
print (",".join(numbers))