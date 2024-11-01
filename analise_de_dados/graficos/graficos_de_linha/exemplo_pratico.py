import matplotlib.pyplot as plt
import pandas as pd

#Suponha que você trabalhe em uma empresa de varejo chamada "SuperStore"
# e seja responsável por analisar as vendas de dois tipos de produtos: eletrônicos e vestuário.

dados = {
    'Ano': [2019,2020,2021,2022,2023],
    'Eletrônicos': [100,120,150,140,160],
    'Vestuário': [80,90,110,100,120]
}

df_vendas = pd.DataFrame(dados)

anos = df_vendas['Ano']
vendas_eletronicos = df_vendas['Eletrônicos']
vendas_vestuario = df_vendas['Vestuário']

plt.plot(anos,vendas_eletronicos, linestyle = '--', marker = 'o', label = 'Vendas de Eletrônicos')
plt.plot(anos,vendas_vestuario, linestyle = '--', marker = '>', label = 'Vendas de Roupas')

plt.xlabel('Eixo do Ano')
plt.ylabel('Eixo de vendas')
plt.title('Comparação entre vendas de eletrônicos e Vestuários')

plt.legend()
plt.show()
