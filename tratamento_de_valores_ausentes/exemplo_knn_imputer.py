"""
KNNImputer
Técnica avançada de imputação de valores ausentes
Utiliza um algoritmo KNN (K-nearest Neighbors) para estimativa dos valores faltantes

Leva em consideração a relação de estrutura de dados para preencher os valores ausentes,
Tornando as estimativas mais precisas e realistas

"""
from sklearn.impute import KNNImputer
import pandas as pd
import numpy as np

# Dict de dados com notas de estudantes
dados = {
    'Matematica': [80, 90, np.nan, 95],
    'Portugues': [60, 65, 56, np.nan],
    'Fisica': [80, 57, 80, 78],
    'Biologia': [78, 83, 67, np.nan]
}

df = pd.DataFrame(dados)

# Criando uma instância do KNNImputer usando a estratégia da distância euclidiana

imputer = KNNImputer(n_neighbors=2)
df_imputer = imputer.fit_transform(df)
df_imputer = pd.DataFrame(df_imputer, columns=df.columns)

print(f"Conjunto Original:\n {df}")
print(f"Conjunto com KNNImputer:\n {df_imputer}")
