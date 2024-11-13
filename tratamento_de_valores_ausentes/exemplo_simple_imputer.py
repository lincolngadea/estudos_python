from sklearn.impute import SimpleImputer
import pandas as pd

# Dict de dados com valores ausentes
dados = {
    'A': [1, 2, None, 4, 5],
    'B': [None, 2, 3, 4, 5],
    'C': [1, 2, 3, 4, None]
}

df = pd.DataFrame(dados)

# Cria uma instância de SimpleImputer com a estratégia de substituição da média
imputer = SimpleImputer(strategy='mean')

# Aplicando o imputer aos valores ausentes do conjunto de dados
# Tira a média da coluna para substituir nos campos ausentes
df_imputer = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

print(f"Conjunto Original:\n {df}")
print(f"Conjunto com Imputer:\n {df_imputer}")