# -*- coding: utf-8 -*-
"""
Created on Wed Apr 08 17:20:00 2023

@author: MVREAL
"""
#
# Secao is a Python Class for the design and verification of reinforced concrete polygonal cross-secions
#
import numpy as np
import matplotlib.pyplot as plt
#
#
class Secao():
    """
    Secao is a Python Class for the evaluation of the geometrical properties polygonal cross-secions
    """

    def __init__(self, xc=[], yc=[]):
        """Initialize the variables"""
        self.xc = xc[:]  # x coordinates of the poligonal vertices
        self.yc = yc[:]  # y coordinates of the poligonal vertices
        
   
        
    @property
    def props(self):
        
        x = np.array(self.xc)
        y = np.array(self.yc)

         
        #
        G00 = 0.00
        G01 = 0.00
        G10 = 0.00
        G02 = 0.00
        G20 = 0.00
        G11 = 0.00
        n = len(x)
        #
        for i in range(n-1):
            
            dx = x[i+1] - x[i]
            dy = y[i+1] - y[i]
            #
            G00 = G00 + dy*(dx/2 + x[i])
            G01 = G01 + dy**2*dx/3 + dy*(dy*x[i]/2 + dx*y[i]/2 + x[i]*y[i])
            G10 = G10 + dy*(dx**2/6 + dx*x[i]/2 + x[i]**2/2)
            G02 = G02 + dy**3*dx/4 + dy**2*(dy*x[i]/3 + 2*dx*y[i]/3) + dy*(dy*x[i]*y[i] + dx*y[i]**2/2 + x[i]*y[i]**2)
            G20 = G20 + dy*(dx**2/12+dx**2*x[i]/3+dx*x[i]**2/2+x[i]**3/3)
            G11 = G11 + (dx*dy)**2/8 + dy*(dx*dy*x[i]/3 + dy*x[i]**2/4 + dx**2*y[i]/6 + dx*x[i]*y[i]/2 + y[i]*x[i]**2/2)
        #
        A = G00
        Sx = G01
        Sy = G10
        Jx = G02
        Jy = G20
        Jxy = G11
        #
        xg = Sy/A
        yg = Sx/A
        Jxg = Jx - A*yg**2
        Jyg = Jy - A*xg**2
        Jxgyg = Jxy - A*xg*yg
        #
        print('A =',A)
        print('Sx =',Sx)
        print('Sy =',Sy)
        print('Jx =',Jx)
        print('Jy =',Jy)
        print('Jxy =',Jxy)
        #
        print('xg =',xg)
        print('yg =',yg)
        print('Jxg =',Jxg)
        print('Jyg =',Jyg)
        print('Jxgyg =',Jxgyg)
        #
        plt.plot(x,y)
        
