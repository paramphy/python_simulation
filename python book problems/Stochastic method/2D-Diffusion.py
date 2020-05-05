# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 10:03:08 2020

@author: param
"""

import sys
from pylab import *
from random import randint


figure(figsize=(10,10))

atoms = ones([400,2])*100

line, = plot(atoms[:,0], atoms[:,1], 'ro')
xlim(0,200)
ylim(0,200)
draw()
wait = input ("Press return to continue")


N = 10000
for i in range(N):
    
    for j in range(400):
        
        atoms[j,0] += randint(-1,1)
        atoms[j,1] += randint(-1,1)
        
        x,y = (atoms[j,0], atoms[j,1])
        if x == 200:
            atoms[j,0] = 198
        elif x == 0:
            atoms[j,0] = 2
        if y == 200:
            atoms[j,1] = 198
        elif y == 0:
            atoms[j,1] = 2  
    line.set_xdata(atoms[:,0])
    line.set_ydata(atoms[:,1])
    draw()
    
wait = input("Press return to exit")

