# Use the darkgrid theme for seaborn
import seaborn as sns
sns.set_theme(style="darkgrid")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# Sample data
from tkinter import W

x = [25,16,12,8]
y = [175.9377778,65.87555556,19.30577778,3.828444444]
z = [167.7332674,64.7790966,20.48796571,4.449390043]
w = [183.6182336,65.46533713,18.83190883,3.138651472]
h = [187.6065891,67.91989664,17.1996124,3.05878553]
q = [154.642,65.102,36.612,16.262]

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

# Dotted line with asterisk markers
sns.lineplot(x=x, y=q, linestyle='--', marker='v', markersize=12, label='True Activity', color='red') 

plt.title(' ') # Add a title
plt.xlabel('Cylinder Diameter', fontsize='20') # x-axis name
plt.ylabel('Activity (kBq)', fontsize='20') # x-axis name
plt.legend(loc='upper left', fontsize='15') # Add a legend
plt.show() # Display the graph