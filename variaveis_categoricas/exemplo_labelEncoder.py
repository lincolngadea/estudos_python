"""
O LabelEncoder é usado quando temos variáveis categóricas com categorias diferentes e precisamos
converte-las em valores numéricos para serem processadas pelos algorítmos de linguagem de máquina.
"""
from sklearn.preprocessing import LabelEncoder
import pandas as pd

# Dados de exemplo

dados = {
    'tamanho': ['pequeno', 'médio', 'grande', 'médio', 'pequeno'],
    'intensidade': ['fraco', 'médio', 'forte', 'forte', 'fraco'],
    'classificacao': ['baixo', 'médio', 'alto', 'médio','baixo']
}

df = pd.DataFrame(dados)
print(f"DataFrame Original:\n{df}")

# Instanciando o LabelEncoder
encoder = LabelEncoder()

# Aplicando o LabelEncoder em cada coluna
for coluna in df.columns:
    df[coluna]=encoder.fit_transform(df[coluna])

print(f"DataFrame Codificado:\n{df}")
