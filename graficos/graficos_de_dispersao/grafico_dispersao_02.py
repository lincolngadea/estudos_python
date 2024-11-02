import pandas as pd
import matplotlib.pyplot as plt

altura = [165, 170, 175, 168, 172, 180, 160, 155, 162, 175]
peso = [60, 65, 70, 63, 68, 75, 55, 50, 58, 70]

# plt.scatter(altura,peso)
# plt.xlabel('Altura (cm)')
# plt.ylabel('Peso (Kg)')
# plt.title('Relação entre Altura e Peso')
# plt.show()

plt.scatter(altura,peso, c='red', marker='^')
plt.xlabel('Altura (cm)')
plt.ylabel('Peso (Kg)')
plt.title('Relação entre Altura e Peso')
plt.show()