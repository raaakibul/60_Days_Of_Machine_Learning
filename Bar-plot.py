#  Data Visualization - 
# @matplotlib

#  Bar Plots 

# With Pyplot, you can use the bar() function to draw bar graphs.

# # Draw 4 bars

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A","B","C","D"])
y = np.array([1,8,4,5])

plt.bar(x,y)
plt.show()
