# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 17:13:24 2019

@author: hannahrajarao
"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
# Data for Youngs (lengths in nanometers)
a = 1500.0
d = a*3
lamb = 650.0
# Data for plotting
theta = np.linspace(-np.pi/4.0, np.pi/4.0, np.pi//0.001)

delta = (2.0 * np.pi / lamb) * d * np.sin(theta)
bigIdouble = (np.cos(delta/2.0))**2

beta = (np.pi / lamb)*a*np.sin(theta)
bigIsingle = (np.sin(beta)/beta)**2
deg = theta*(180/np.pi)
fig, ax = plt.subplots()
ax.plot(deg, bigIdouble, 'm')
ax.plot(deg, bigIsingle, 'b')
ax.plot(deg, bigIdouble*bigIsingle, 'r')
ax.set(xlabel= 'Theta', ylabel='Intensity (I)', title='Intensity for Finite Width Single Slit')
ax.grid()
plt.legend(['Interference','Diffraction','Together'], bbox_to_anchor = [1,1])
plt.show()