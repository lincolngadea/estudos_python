"""
O OrdinalEncoder transforma variáveis categóricas em dados numéricos e atribui valores ordinais
às categorias

Vantagens:
- Mantem a ordem entre as categorias, considerando as informações ordenadas durante a análise dos dados

É uma boa opção para codificar categorias com uma ordem natural, como níveis de educação (Ensino fundamental, médio, superior)
ou classificação de sentimentos (baixo, médio, alto)
"""

from sklearn.preprocessing import OrdinalEncoder
import pandas as pd

# Dados de exemplo
dados = {
    'Nome': ['Leandro', 'Daniele', 'Gilberto', 'Roberta', 'João'],
    'Idade': [32, 27, 54, 39, 68],
    'rating_satisfacao': ['Satisfeito', 'Muito Satisfeito', 'Muito Insatisfeito', 'Insatisfeito', 'Neutro']
}

df = pd.DataFrame(dados)

# Criando a ordem de grandeza das categorias dos dados
categorias = [ 'Muito Insatisfeito', 'Insatisfeito','Neutro', 'Satisfeito','Muito Satisfeito']

# Instanciando o OrdinalEncoder
encoder = OrdinalEncoder(categories=[categorias])
df['rating_satisfacao_encoder'] =encoder.fit_transform(df[['rating_satisfacao']])

print(df)