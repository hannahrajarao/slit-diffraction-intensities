# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 16:11:26 2019

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
bigI = (np.cos(delta/2.0))**2
dovlamsintheta = (d / lamb) * np.sin(theta)
fig, ax = plt.subplots()
ax.plot(dovlamsintheta, bigI, 'r')
ax.set(xlabel= 'Position*(d/lambda)*sin(theta)', ylabel='Intensity (I)', title='Young\'s Double Slit Intensity')
ax.grid()
fig.savefig("youngs_ds.png")
plt.show()