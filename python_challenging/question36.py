#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import math

print(random.random()*100)
print(random.random()*100-5)
print (random.choice([i for i in range(11) if not i&1]))
print (random.choice([i for i in range(201) if i%5==0 and i%7==0]))
print (random.sample(range(100), 5))
print (random.sample([i for i in range(100,201) if not i&1], 5))
print (random.randrange(7,16))