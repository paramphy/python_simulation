# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 17:43:37 2020

@author: param
"""

""" Program to model 1-D random walk"""

from random import random
from pylab import *

N = 2000
x = zeros([N])
t = range(N)

for i in range(1,N):
    if choice(['forward', 'back']) == 'back':
        x[i] = x[i-1] - 1
    else:
        x[i] = x[i-1] + 1
    
    RMS = array([sqrt(i*i) for i in x])
    
plot(t, x, '-b')
plot(t, RMS, 'g-')
    
show()
    