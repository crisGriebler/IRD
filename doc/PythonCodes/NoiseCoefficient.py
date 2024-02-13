# Use the darkgrid theme for seaborn
import seaborn as sns
sns.set_theme(style="darkgrid")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# Sample data
from tkinter import W

x = [25,16,12,8]
y=[0.1464174455,0.208820993,0.1165524997,0.1070987231]
z=[0.2181818182,0.2391559203,0.1749611198,0.1249511909]
w=[0.1133757962,0.1403201052,0.07707774799,0.0828892836]
h=[0.1310861423,0.1376889849,0.1325443787,0.08242664029]

# Set Seaborn style
plt.figure(figsize=(8, 6))

# Solid line with circle markers
sns.lineplot(x=x, y=y, linestyle='-', marker='o', markersize=8, label='Triple Energy window', color='black') 

# Dashed line with square markers
sns.lineplot(x=x, y=z, linestyle='-', marker='o', markersize=8, label='89kv(24%)kV', color='blue') 

# Dash-dot line with triangle up markers
sns.lineplot(x=x, y=w, linestyle='-', marker='o', markersize=8, label='156(20%)kV', color='purple') 

# Dotted line with asterisk markers
sns.lineplot(x=x, y=h, linestyle='-', marker='o', markersize=8, label='270(20%)kV', color='orange') 

plt.title(' ') # Add a title
plt.xlabel('Cylinder diameter') # x-axis name
plt.ylabel('NoiseCoefficient') # x-axis name
plt.legend(loc='upper left') # Add a legend
plt.show() # Display the graph