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
    Secao is a Python Class for the design and verification of reinforced concrete polygonal cross-secions
    """

    def __init__(self, op=[], gamma_c=1.4, gamma_s=1.15, nc=[], nrc=[], ns=[], na=[], maxd=[], mayd=[], xc=[], yc=[], fck=[], nvrc=[], xs=[], ys=[], fyk=[], perc=[]):
        """Initialize the variables"""
        self.op = op # solution option: 1 = design of the reinforcement area, 2 = verification of the cross-section capacity
        self.gamma_c = gamma_c # concrete safety factor, usually equal to 1.4
        self.gamma_s = gamma_s # steel safety factor, usually equal to 1.15
        self.nc = nc # number of polygonal vertices
        self.nrc = nrc # number of different concrete regions in the cross-section
        self.ns = ns # number os steel bars
        self.na = na # design value of the external normal force: positive for tension force and negative for compression force
        self.maxd = maxd # design value of the external bending moment in relation to the x axis
        self.mayd = mayd # design value of the external bending moment in relation to the x axis
        self.xc = xc[:]  # x coordinates of the poligonal vertices
        self.yc = yc[:]  # y coordinates of the poligonal vertices
        self.fck = fck[:] # fck of the different cross-section regions
        self.nvrc = nvrc[:] # number of vertices of each different concrete region
        self.xs = xs[:]  # x coordinates of the reinforcement bars
        self.ys = ys[:]  # y coordinates of the reinforcement bars
        self.fyk = fyk[:] # fyk of the reinforcement bar
        self.perc = perc[:] # pencentage stell bar cross-section area of the total steel area in the cross-section
        


        
        
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
        
