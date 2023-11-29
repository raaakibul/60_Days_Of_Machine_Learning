# Data Visualization with Matplotlib

# Pie Charts

# Lets create a pie chart👇

# With Pyplot, you can use the pie() function to draw pie charts.

# A simple pie chart:

import matplotlib.pyplot as plt
import numpy as np

pie_plot = np.array([20,25,15,20,20])
pie_labels = ["Bananas", "Apples","Mangoes","Dates","Limes"]
pie_explodes = [0.2,0,0,0,0]

plt.pie(pie_plot, labels=pie_labels, explode=pie_explodes)
plt.legend()
plt.show()
