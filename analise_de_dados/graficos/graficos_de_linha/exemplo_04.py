from cProfile import label

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]
y3 = [3, 6, 9, 12, 15]

# Create stylized line plots

plt.plot(x, y1, linestyle='--', marker='o', label='Series 1')  # Changed 'Serie' to 'Series'
plt.plot(x, y2, linestyle=':', marker='s', label='Series 2')   # Changed 'Serie' to 'Series'

plt.xlabel('X Axis')  # Changed 'Eixo X' to 'X Axis'
plt.ylabel('Y Axis')  # Changed 'Eixo Y' to 'Y Axis'
plt.title('Styled Line Plot with Markers')  # Changed 'Style line Graphic and markers' to 'Styled Line Plot with Markers'

plt.legend()

plt.show()