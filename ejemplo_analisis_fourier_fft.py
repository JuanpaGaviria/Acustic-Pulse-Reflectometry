#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 21:22:56 2022

@author: whadymacbook2016
"""
import numpy as np
import matplotlib.pyplot as plt
nsample=10000
t=np.linspace(0,10,nsample)
dt=10/(nsample-1)
f1=1
f2=2
f3=3
f4=15
y1=np.sin(2*np.pi*f1*t)
y2=np.sin(2*np.pi*f2*t)
y3=np.sin(2*np.pi*f3*t)
y4=np.sin(2*np.pi*f4*t)
y=y1+y2+y3+y4

ft=np.fft.fft(y)
n = ft.size
ftfreq=np.fft.fftfreq(n,d=dt)
ftr=ft.real
fti=ft.imag
plt.figure()
plt.plot(ftfreq,ftr)
#plt.plot(fti)
plt.figure()
plt.plot(t,y)




