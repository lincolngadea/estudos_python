import matplotlib.pyplot as plt
import pandas as pd
from pyparsing import alphas

anos = [2010, 2011, 2012, 2013, 2014, 2015, 2016]
variavel = [100, 120, 150, 130, 140, 160, 180]

# Cria Gráfico de área simples
plt.fill_between(
    anos,
    variavel,
    color='blue',
    alpha=0.3
)

# Configuração de eixos e título
plt.xlabel('Ano')
plt.ylabel('Variável')
plt.title('Avaliação da variável ao longo do tempo')

# Exibe o gráfico
plt.show()