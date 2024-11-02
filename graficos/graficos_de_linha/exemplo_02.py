from cProfile import label

import pandas as pd
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Plot customization

plt.plot(x, y, label='Series 1')  # Changed 'Série' to 'Series'
plt.ylabel('Y Axis')  # Changed 'Eixo Y' to 'Y Axis'
plt.xlabel('X Axis')  # Changed 'Eixo X' to 'X Axis'
plt.title('Customized Plot')  # Changed 'Gráfico Customizado' to 'Customized Plot'
plt.legend()

plt.show()