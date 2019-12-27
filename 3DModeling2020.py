#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib import cm
from tqdm import trange

iterations = 50000

cube = np.zeros((22, 22, 1000))

r = 9
center_x = 11
center_y = 11

for k in trange(5, 996, 1):
    for i in range(len(cube)):
        for j in range(len(cube[0])):
            radius = np.sqrt((center_x - i)**2 + (center_y - j)**2)
            if (radius <= r):
                cube[i][j][k] = 1  
                

mask = cube.copy()

for k in trange(5, 996, 1):
    cube[11, 11, k] = 20
    cube[11, 10, k] = 20
    cube[11, 12, k] = 20
    cube[10, 11, k] = 20
    cube[12, 11, k] = 20

    mask[11, 11, k] = 0
    mask[11, 10, k] = 0
    mask[11, 12, k] = 0
    mask[10, 11, k] = 0
    mask[12, 11, k] = 0


np.save("cubeCylinder2020", cube)
np.save("maskCylinder2020", mask)
    
for k in trange(iterations):
    for i in range(len(cube)):
        for j in range(len(cube[0])):
            for k in range(len(cube[0][0])):
                if (mask[i][j][k] == 1):
                    cube[i][j][k] = (cube[i, j, k-1] +
                                     cube[i, j, k+1] + 
                                     cube[i, j-1, k] + 
                                     cube[i, j+1, k] + 
                                     cube[i-1, j, k] + 
                                     cube[i+1, j, k])/6    
                    

np.save("cylinderModel2020", cube)
plt.figure()
plt.pcolormesh(cube[:, :, 500], cmap=cm.get_cmap("viridis", 20), rasterized=True, vmin=0, vmax=20)
plt.colorbar()


cube = np.zeros((22, 22, 22))
r = 9
center_x = 11
center_y = 11
center_z = 11

for i in trange(len(cube)):
    for j in range(len(cube[0])):
        for k in range(len(cube[0][0])):
            radius = np.sqrt((center_x - i)**2 + (center_y - j)**2 + (center_z - k)**2)
            if (radius <= r):
                cube[i][j][k] = 1 
                

mask = cube.copy()

cube[11, 11, 11] = 20
cube[11, 11, 10] = 20
cube[11, 11, 12] = 20
cube[11, 10, 11] = 20
cube[11, 12, 11] = 20
cube[10, 11, 11] = 20
cube[12, 11, 11] = 20

mask[11, 11, 11] = 0
mask[11, 11, 10] = 0
mask[11, 11, 12] = 0
mask[11, 10, 11] = 0
mask[11, 12, 11] = 0
mask[10, 11, 11] = 0
mask[12, 11, 11] = 0

np.save("cubeSphere2020", cube)
np.save("maskSphere2020", mask)

for k in trange(iterations):
    for i in range(len(cube)):
        for j in range(len(cube[0])):
            for k in range(len(cube[0][0])):
                if (mask[i][j][k] == 1):
                    cube[i][j][k] = (cube[i, j, k-1] +
                                     cube[i, j, k+1] + 
                                     cube[i, j-1, k] + 
                                     cube[i, j+1, k] + 
                                     cube[i-1, j, k] + 
                                     cube[i+1, j, k])/6 

np.save("sphereModel2020", cube)
plt.figure()
plt.pcolormesh(cube[:, :, 11], cmap=cm.get_cmap("viridis", 20), rasterized=True, vmin=0, vmax=20)
plt.colorbar()


# In[ ]:




