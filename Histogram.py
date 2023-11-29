#  Data Visualization with Matplotlib

# Histograms

# A histogram is a graphical representation of frequency distributions.

# It is a graph that displays the number of observations within each interval.

# Lets create a histogram

import matplotlib.pyplot as plt
import numpy as np
x = np.random.normal(170,10,250)

plt.hist(x)
plt.show()
# print(x)
