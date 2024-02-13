# Use the darkgrid theme for seaborn
import seaborn as sns
sns.set_theme(style="darkgrid")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# Sample data
from tkinter import W

x = [25,16,12,8]
y = [52.64095745,21.86135693,19.05175439,5.521794872]
z = [65.2224359,38.5245098,27.61777778,8.434375]
w = [43.4494382,17.45189873,17.24347826,4.721428571]
h = [37.23269231,9.780465116,7.395833333,3.788]
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
plt.xlabel('Cylinder diameter',fontsize='20') # x-axis name
plt.ylabel('Signal-Noise Ratio',fontsize='20') # x-axis name
plt.legend(loc='upper left',fontsize='15') # Add a legend
plt.show() # Display the graph