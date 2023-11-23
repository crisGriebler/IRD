# Use the darkgrid theme for seaborn
import seaborn as sns
sns.set_theme(style="darkgrid")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# Sample data
from tkinter import W

x = [25,16,12,8]
y = [1.14,1.01,0.53,0.24]
z = [1.08,1.00,0.56,0.27]
w = [1.19,1.01,0.51,0.19]
h = [1.21,1.04,0.47,0.19]


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
plt.xlabel('Cylinder diameter', fontsize='20') # x-axis name
plt.ylabel('Recovery Coefficient', fontsize='20') # x-axis name
plt.legend(loc='lower right'  , fontsize='15') # Add a legend
plt.show() # Display the graph