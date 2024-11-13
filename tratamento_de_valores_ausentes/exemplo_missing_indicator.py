import pandas as pd
from sklearn.impute import MissingIndicator
import numpy as np

# Dict de dados com notas de estudantes
dados = {
    'Matematica': [80, 90, np.nan, 95],
    'Portugues': [60, 65, 56, np.nan],
    'Fisica': [80, 57, 80, 78],
    'Biologia': [78, 83, 67, np.nan]
}

df = pd.DataFrame(dados)

print("\nAntes do Imputer de dados:\n",df)

# Criando uma instância do Missing Indicator
indicator = MissingIndicator(features='all')

# Aplicando os imputes aos valores ausentes do conj de dados
indicator.fit(df)
df_indicator = indicator.transform(df)
df_indicator = pd.DataFrame(df_indicator, columns=df.columns)

print("\nApós o Imputer de dados:\n",df_indicator)