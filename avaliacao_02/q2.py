"""
Qual é a cor de cabelo mais comum entre os clientes?
"""
import pandas as pd

#Carrega dados
dados_cli = pd.read_csv('./dados/clientes_caracteristicas_fisicas.csv', sep=',')

df_dados_cli = pd.DataFrame(dados_cli)

df_dados_cli_cor_cabelo = df_dados_cli['Cor do Cabelo']

count_cli_cor_cabelo = df_dados_cli_cor_cabelo.value_counts()
cor_mais_comum = count_cli_cor_cabelo.idxmax()
freq_mais_comum = count_cli_cor_cabelo.max()

print(f"A cor {cor_mais_comum} aparece {freq_mais_comum} vezes")