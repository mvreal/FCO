# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 17:37:00 2023

@author: MVREAL
"""
#
# Calculates the expoent of the concrete compression curve
#
import numpy as np
import matplotlib.pyplot as plt
#
#
n = np.zeros(1000)
fck = np.array(np.linspace(20,90,1000))
#
i = -1
for fc in fck:
    i += 1
    if fc<=50:
        n[i] = 2.00
        
    else:
        n[i] = 1.40 + 23.40*((90 - fc)/100)**4

plt.plot(fck,n,color ='red',label='$n(fck)$')
plt.xlabel(r'$f_{ck}$(MPa)')
plt.ylabel(r'$n$')
plt.xlim(20,90)
plt.ylim(1.0,3.0)
plt.grid()
plt.legend(loc='upper right')
plt.show()

