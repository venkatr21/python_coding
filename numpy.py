# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 10:15:05 2019

@author: Venkat
"""

import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,10,0.2)
y=np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()