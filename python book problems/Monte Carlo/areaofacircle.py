# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from random import random
from math import sqrt

N = 1000000
count = 0
for j in range(N):
    point =(random(), random(), random())
    if point[0]*point[0] + point[1]*point[1] + point[2]*point[2]<1:
        count = count+1

Answer = float(count)/float(N)

Answer = 4 * Answer 
 
print (Answer, 4*sqrt(N)/float(N))