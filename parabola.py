# -*- coding: utf-8 -*-
"""
Created on Tue Apr 04 17:00:00 2023

@author: MVREAL
"""
#
# Calculates the coeficients of the concrete compression curve
#
import numpy as np
import matplotlib.pyplot as plt
#
#
fck = np.array([50,60,70,80,90])
a1 = np.zeros(len(fck))
a2 = np.zeros(len(fck))
#
i = -1
for fc in fck:
    i += 1
    if fc<=50.00:
        n = 2.00
        ec2 = 0.002
        
    else:
        n = 1.40 + 23.40*((90.00 - fc)/100.00)**4
        ec2 = (2.00 + 0.085*(fc - 50.00)**0.53)/1000.

    scd = 0.85 * fc / 1.4

    npoints = 1000

    # Evaluation of y = f(x)
    x = np.linspace(0.00, ec2, npoints)
    y = (1.00 - (1.00 - x/ec2)**n)

    #Summations
    sx2 = 0.00
    sx3 = 0.00
    sx4 = 0.00
    sxy = 0.00
    sx2y = 0.00

    for j in range(npoints):
        
        sx2 += x[j]**2
        sx3 += x[j]**3
        sx4 += x[j]**4
        sxy += x[j]*y[j]
        sx2y += x[j]**2*y[j]

    # Coeficients a1 and a2

    a1[i] = (sx2y - sx4*sxy/sx3)/(sx3 - sx2*sx4/sx3)

    a2[i] = (sx2y - a1[i] * sx3)/sx4

    print('fck = {0:0.0f} MPa a2 = {1:0.0f} a1 = {2:0.2f}'.format(fck[i],a2[i],a1[i]))

    y2 = scd*(a2[i]*x**2+a1[i]*x)
    yn = scd*y

plt.plot(1000*x,yn,color ='red',label='n = 1.4')
plt.plot(1000*x,y2,color ='blue',label='n = 2')
plt.title(r'$f_{ck}$ = 90 MPa')
plt.xlabel(r'$\epsilon_{c} ‰$')
plt.ylabel(r'$\sigma_{cd}$')
plt.grid()
plt.legend(loc='lower right')
plt.show()
    
    

