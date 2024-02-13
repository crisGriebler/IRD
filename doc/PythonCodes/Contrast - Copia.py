# Use the darkgrid theme for seaborn
import seaborn as sns
sns.set_theme(style="darkgrid")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# Sample data
from tkinter import W

x = [25,16,12,8]
y=[8.150650289,4.613359337,3.220529598,1.59137718]
z = [15.50834165,10.2133646,5.832037325,2.053885201]
w = [6.363384189,3.4302838,2.329088472,1.391355832]
h = [5.316192316,2.98902762,2.26035503,1.312232113]

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
plt.ylabel('Contrast', fontsize=20) # x-axis name
plt.legend(loc='upper left', fontsize='15') # Add a legend
plt.show() # Display the graph