import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

idade_masc = np.random.normal(30, 5, 100)
idade_fem = np.random.normal(35, 5, 100)

# Data Frame
df = pd.DataFrame({'Masculino': idade_masc, 'feminino': idade_fem})

# Gráfico de boxplot
df.plot(kind='box', vert=False, patch_artist=True, widths=0.5)

# Rótulos e títulos
plt.xlabel('Idade')
plt.ylabel('Gênero')

# Exibição do gráfico
plt.show()
