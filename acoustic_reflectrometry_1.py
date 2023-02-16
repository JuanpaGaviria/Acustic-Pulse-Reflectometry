#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 09:12:14 2022

@author: whadyimac
First trial acoustic reflectometry
"""
import numpy as np
import matplotlib.pyplot as plt

N=5  #segments
S=np.zeros(N+1) #cross sectional areas
D=np.zeros(N+1) #Diameters of each segment
L=np.zeros(N) #segment length
Z=np.zeros(N+1) #Acoustic impedance of each segment


Lp=1 #pipe length
dx=Lp/N
d=1 #density
c=1 #acoustic wave velocity
#w=0 #frequency

L[0:N]=dx
D[0:4]=1e-2
D[4:7]=2e-2
D[7:11]=3e-2

for i in range (0,N+1):
    S[i]=np.pi*D[i]**2/4
    Z[i]=d*c/S[i]
def iir(w):
    M=[]#list of impedance matrices
    for j in range (0,N):
        Mi=np.zeros((2,2))
        Mi[0,0]=(Z[j+1]+Z[j])/(2*Z[j+1])
        Mi[0,1]=(Z[j+1]-Z[j])/(2*Z[j+1])
        Mi[1,0]=(Z[j+1]-Z[j])/(2*Z[j+1])
        Mi[1,1]=(Z[j+1]+Z[j])/(2*Z[j+1])
        k=w/c
        Mdelay=np.zeros((2,2),dtype=complex)
        Mdelay[0,0]=np.exp(complex(0,k*L[j]))
        Mdelay[1,1]=np.exp(complex(0,-k*L[j]))
        M.append(np.matmul(Mi,Mdelay))
    Mp=np.identity(2) #product matrix
    for j in range(0,N):
        Mp=np.matmul(Mp,M[j])
        
    ir=Mp[1,0]/Mp[0,0] #input impulse response simple case semi infinite endtube
#    print(np.real(ir),np.abs(ir))
    return ir

ndata=100
w=np.linspace(0,60,ndata)
response=np.zeros(ndata,dtype=complex)
for i in range (0,ndata):
    response[i]=iir(w[i])
ift=np.fft.ifft(response)


plt.plot(w,response)
plt.figure()
plt.plot(np.real(ift))
plt.plot(np.imag(ift))
    


