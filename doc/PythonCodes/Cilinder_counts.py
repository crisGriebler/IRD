# Use the darkgrid theme for seaborn
import seaborn as sns
sns.set_theme(style="darkgrid")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# Sample data
from tkinter import W

x = [25,16,12,8]
y = [22561,9462,3150,1159]
z = [10876,4356,1500,526]
w = [4588,1946,695,235]
h = [7154,3160,955,398]

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
plt.ylabel('Counts', fontsize=20) # x-axis name
plt.legend(loc='upper left', fontsize='15') # Add a legend
plt.show() # Display the graph