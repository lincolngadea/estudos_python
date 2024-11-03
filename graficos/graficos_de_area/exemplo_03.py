import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = {
    'Data': pd.date_range(start='2023-01-01', end='2023-12-31', freq='D'),
    'Vendas': np.random.randint(20, 50, size=365),
    'Lucro': np.random.uniform(8, 15, size=365)
}

# Criando o DataFrame
df = pd.DataFrame(data)

# Cores suaves e transparentes
cores = ['#FF7F50', '#6A5ACD']

# Criação da figura e eixos personalizados
fig, ax = plt.subplots(figsize=(10,5))

# Plotar gráfico de área com cores suaves e transparentes
df.plot(x='Data', y=['Vendas','Lucro'], kind='area', color=cores, alpha=0.5, ax=ax)

# Personalização do gráfico
ax.set_title('Gráfico de área - Variáveis ao longo do tempo')
ax.set_xlabel('Anos')
ax.set_ylabel('Valores')

# Exibe o gráfico
plt.show()
