"""
Qual é a proporção de clientes com tatuagens e piercings?
"""
from fractions import Fraction
import pandas as pd

# Carga dos dados
dados_cli = pd.read_csv('./dados/clientes_caracteristicas_fisicas.csv', sep=',')

df_cli = pd.DataFrame(dados_cli)

# print(df_cli.columns)

total_tatuagens = (df_cli['Tatuagens'] > 0).sum()
total_piercings = (df_cli['Piercings'] > 0).sum()
total_geral = len(df_cli)

proporcao_tatuagens = total_tatuagens / total_geral
proporcao_piercings = total_piercings / total_geral

print(f"Proporcao Tatoo: {proporcao_tatuagens}")
print(f"Proporcao Piercing: {proporcao_piercings}")