# Data Visualization - Matplotlib

# Creating Scatter Plots

# With Pyplot, you can use the scatter() function to draw a scatter plot.

# The scatter() function plots one dot for each observation.

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,14,16,7,8,9,10,14,10,13,14,15])
y = np.array([88,87,98,81,86,81,84,96,89,98,94,86,82])

plt.scatter(x,y)
plt.show()
