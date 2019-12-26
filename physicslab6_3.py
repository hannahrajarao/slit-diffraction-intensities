# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 16:28:08 2019

@author: hannahrajarao
"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
# Data for Youngs (lengths in nanometers)
a = 1500.0
lamb_b = 350.0
lamb_r = 700.0
# Data for plotting
theta = np.linspace(-np.pi/2.0, np.pi/2.0, np.pi//0.001)
beta_b = (np.pi / lamb_b)*a*np.sin(theta)
bigIblue = (np.sin(beta_b)/beta_b)**2
beta_r = (np.pi / lamb_r)*a*np.sin(theta)
bigIred = (np.sin(beta_r)/beta_r)**2
dovlamsintheta = (a / lamb_b) * np.sin(theta)

fig, ax = plt.subplots()
ax.plot(dovlamsintheta, bigIred, 'r')
ax.plot(dovlamsintheta, bigIblue, 'b')

ax.set(xlabel= 'Position*(d/lambda)*sin(theta)', ylabel='Intensity (I)', title='Single Finite Width Slit Intensity')
ax.grid()
plt.legend(['Red light (700 nm)','Blue light (350 nm)'], bbox_to_anchor = [1,1])
plt.show()