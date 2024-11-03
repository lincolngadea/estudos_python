from cProfile import label

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Definindo o número de linhas
num_linhas = 20

# Gerando dados aleatórios para as colunas
np.random.seed(42)  # Para reprodutibilidade dos dados
anos = np.random.randint(2000, 2023, size=num_linhas)
receita_produto_1 = np.random.randint(20000, 100000, size=num_linhas)
receita_produto_2 = np.random.randint(20000, 100000, size=num_linhas)

# Calculando a receita total
receita_total = receita_produto_1 + receita_produto_2

# Criando o DataFrame
df = pd.DataFrame({
    'Ano': anos,
    'Receita Produto 1': receita_produto_1,
    'Receita Produto 2': receita_produto_2,
    'Receita Total': receita_total
})

# Criando a figura e os eixos
fig, ax1 = plt.subplots(figsize=(15, 6))

# Plotando as barras
df[['Ano', 'Receita Produto 1', 'Receita Produto 2']].plot(
    x='Ano',
    kind='bar',
    stacked='True',
    ax=ax1,
    color=['blue', 'green'],
    alpha=0.5
)

# Configurando eixos das barras
ax1.set_xlabel('Ano')
ax1.set_ylabel('Receita por Produto')

# Criando um eixo secundário para o gráfico de linhas
ax2 = ax1.twinx()

# Plotando o gráfico de linha
df['Receita Total'].plot(kind='line', marker='o', color='red', ax=ax1, legend=True)
plt.plot(anos,receita_total, color='red', marker='o', label='Receita Total')

# Configurando o eixo secundário
ax2.set_ylabel('Receita Total')

# Título do gráfico
plt.title('Receita Total e por Produto ao longo do anos')

# Ajuste de layout
plt.tight_layout()

# Exibe o gráfico
plt.show()