from cProfile import label

import pandas as pd
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Plot with multiple vectors

y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]
y3 = [3, 6, 9, 12, 15]

plt.plot(x, y1, label='Series 1')  # Changed 'Série' to 'Series'
plt.plot(x, y2, label='Series 2')  # Changed 'Série' to 'Series'
plt.plot(x, y3, label='Series 3')  # Changed 'Série' to 'Series'
plt.ylabel('Y Axis')  # Changed 'Eixo Y' to 'Y Axis'
plt.xlabel('X Axis')  # Changed 'Eixo X' to 'X Axis'
plt.title('Custom Plot')  # Changed 'Custom Graphic' to 'Custom Plot'
plt.legend()

plt.show()