"""
O OneHotEncoder tem a capacidade de pegar uma variável categórica e transformar ela em colunas.
Cria um conjunto de novas colunas binárias, onde cada coluna representa uma categoria única de
variável categórica.

As colunas são preenchidas com valores binários (0 e 1), indicando se a observação pertence ou não
a uma determinada categoria.

A Codificação OneHotEncoder permite que cada categoria seja tratada como uma variável separada,
capturando todas as informações relevantes.

Principal vantagem:
- Não impõe uma uma ordem ou relação de magnitude entre as categorias.
- Cada categoria é representada de forma independente, permitindo que os algorítmos de aprendizado
de máquina identifiquem padrões e relações entre as diferentes categorias.
"""

import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Dados de exemplo
dados = {
    'cor': ['vermelho', 'azul', 'verde', 'vermelho', 'verde'],
    'tamanho': ['pequeno', 'médio', 'grande', 'médio', 'grande'],
    'formato': ['quadrado', 'redondo', 'quadrado', 'redondo', 'quadrado']
}

df = pd.DataFrame(dados)

# Criando a instância do OneHotEncoder
encoder = OneHotEncoder()

# Ajustando e transformando o dado
dados_codificados = encoder.fit_transform(df[['cor','tamanho','formato']]).toarray()

# Criando um dataframe com dados codificados
df_codificado = pd.DataFrame(dados_codificados, columns=encoder.get_feature_names_out(['cor','tamanho','formato']))

# Exibe o Dataframe original
print(f"DataFrame Original: \n{df}")

# Exibe o Dataframe codificado
print()
print(f"Dataframe codificado:\n{df_codificado}")