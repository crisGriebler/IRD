# Use the darkgrid theme for seaborn
from ctypes.wintypes import SIZE
import seaborn as sns
sns.set_theme(style="darkgrid")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# Sample data
from tkinter import W

x = [25,16,12,8]
y = [2768,2051,978.1,728.3]
z = [701.3,426.5,257.2,256.1]
w = [721,567.3,298.4,168.9]
h = [1345.7,1057.2,422.5,303.3]

# Set Seaborn style
plt.figure(figsize=(8, 6))

# Solid line with circle markers
sns.lineplot(x=x, y=y, linestyle='-', marker='o', markersize=8, label='Triple Energy window', color='black') 

# Dashed line with square markers
sns.lineplot(x=x, y=z, linestyle='-', marker='o', markersize=8, label='89 keV', color='blue') 

# Dash-dot line with triangle up markers
sns.lineplot(x=x, y=w, linestyle='-', marker='o', markersize=8, label='156 keV', color='purple') 

# Dotted line with asterisk markers
sns.lineplot(x=x, y=h, linestyle='-', marker='o', markersize=8, label='270 keV', color='orange') 

plt.title(' ') # Add a title
plt.xlabel('Cylinder Diameter', fontsize=20) # x-axis name
plt.ylabel('Background Counts', fontsize=20) # x-axis name
plt.legend(loc='upper left', fontsize='15') # Add a legend
plt.show() # Display the graphpyt