import matplotlib.pyplot as plt
import pandas as pd

categorias = ['A','B','C','D']
valores = [30,25,20,15]
destaques = [0.1,0,0,0] # Lista de destaques para cada fatia (0 = não destacado)

# Configurações de cores
cores = ['blue','green','orange','red']

# Criação de gráfico de pizza com destaque
patches, texts, autotexts = plt.pie(
    valores,
    labels=categorias,
    explode=destaques,
    colors=cores,
    autopct='%1.1f%%'
)

# Personalizaçao do gráfico
plt.title('Distribuição por Categoria')

# Configuração da cor e estilo dos nomes
for text in autotexts:
    text.set_color('white')
    text.set_fontweight('bold')

# Exibe o gráfico
plt.show()
