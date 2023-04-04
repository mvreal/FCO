# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 17:37:00 2023

@author: MVREAL
"""
#
# Calculates the concrete strain limits
#
import numpy as np
import matplotlib.pyplot as plt
#
#
ec2 = np.zeros(1000)
ecu = np.zeros(1000)
fck = np.array(np.linspace(20,90,1000))
#
i = -1
for fc in fck:
    i += 1
    if fc<=50:
        ec2[i] = 2.00
        ecu[i] = 3.50
    else:
        ec2[i] = 2.00 + 0.085*(fc - 50)**0.53
        ecu[i] = 2.60 + 35.00*((90 - fc)/100)**4

plt.plot(fck,ec2,label='$\epsilon_{c2}$')
plt.plot(fck,ecu,label='$\epsilon_{cu}$')
plt.xlabel(r'$f_{ck}$(MPa)')
plt.ylabel(r'$\epsilon_{c}‰$')
plt.xlim(20,90)
plt.ylim(1.0,4.0)
plt.grid()
plt.legend(loc='upper right')
plt.show()

