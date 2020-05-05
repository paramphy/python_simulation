# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 08:35:39 2020

@author: param
"""

"""
Program to model AVERAGE 1-D random walk

"""

from random import choice
from pylab import *
from scipy.optimize import curve_fit

def power(x,a,b):
    return a*x**b

steps = 2000
boys = 20000

x = zeros([steps])
t = range(steps)
x_sum = zeros([steps])
x2_sum = zeros([steps])

for j in range(boys):
    for i in range(1,steps):
        if choice([0,1]):
            x[i] = x[i-1] - 1
        else:
            x[i] = x[i-1] + 1
    for i in range(steps):
        x_sum[i] = x_sum[i] + x[i]
        x2_sum[i] = x2_sum[i] + x[i]**2

x_avg = [float(i)/float(boys) for i in x_sum]
RMS = [sqrt(float(i)/float(boys)) for i in x2_sum]

xlabel("Time (Step number)")
ylabel("Average and RMS position (Steps)")

plot(t,x_avg, 'b-')
plot(t,RMS, 'g-')

popt, pcov = curve_fit(power, t, RMS)

print ("Power fit: y(t) = A*t^B: ")
print ("A = %f +/- %f." % (popt[0], sqrt(pcov[0,0])))
print ("B = %f +/- %f." % (popt[1], sqrt(pcov[1,1])))

plot(t, power(t,popt[0], popt[1]))
show()