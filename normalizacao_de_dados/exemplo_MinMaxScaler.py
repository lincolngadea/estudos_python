"""
O MinMaxScaler é uma técnica de preprocessamento usada na análise de dados e no
treinamento de modelos de aprendizgem de máquina. Ele é usado para normalizar as variáveis
transformando-as para um intervalo específico, geralmente entre 0 e 1. Útil para comparar variáveis
com escalas diferentes, mas que precisam ser comparáveis.

Ele calcula o valor Mínimo e máximo de cada variável e, em seguida, aplica uma transformação linear
aos dados, escalando-os para o intervalo especificado
"""
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Dados de exemplo
dados = {
    'idade':[25,30,35,40,45],
    'salario':[30000,40000,50000,60000,70000],
    'pontuacao':[50,60,70,80,90]
}

df = pd.DataFrame(dados)

# Instanciando o MinMaxScaler
scaler = MinMaxScaler()

# Normaliza os dados
dados_normalizados = scaler.fit_transform(df)
df_normalizados = pd.DataFrame(dados_normalizados, columns=df.columns)

# Dados Originais
print(f"Dados Originais:\n{df}")
print()
# Dados Normalizados
print(f"Dados Normalizados:\n{df_normalizados}")