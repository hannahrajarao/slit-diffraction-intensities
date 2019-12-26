# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 15:48:13 2019

@author: hannahrajarao
"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
# Data for Youngs (lengths in nanometers)
d = 1000.0
lamb = 650.0
# Data for plotting
theta = np.linspace(-np.pi/2.0, np.pi/2.0, np.pi//0.001)
delta = (2.0 * np.pi / lamb) * d * np.sin(theta)
bigI4 = (1/16)*(np.sin(4*delta/2)/np.sin(delta/2))**2
bigI16 = (1/16**2)*(np.sin(16*delta/2)/np.sin(delta/2))**2
bigI256 = (1/16**4)*(np.sin(256*delta/2)/np.sin(delta/2))**2
dovlamsintheta = (d / lamb) * np.sin(theta)
fig, ax = plt.subplots()
ax.plot(dovlamsintheta, bigI4, 'r')
ax.plot(dovlamsintheta, bigI16, 'b')
ax.plot(dovlamsintheta, bigI256, 'k')
ax.set(xlabel= 'Position*(d/lambda)*sin(theta)', ylabel='Intensity (I)', title='Youngs Slit Intensity for Various N Values')
ax.grid()
plt.legend(['N=4','N=16','N=256'],bbox_to_anchor = [1,1])
plt.show()