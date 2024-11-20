"""
O RobustScaler é uma técnica de pré-processamento utilizada na análise de dados e no treinamento
de modelos de aprendizado de máquina.

É usado para padronizar as variáveis, tornando-as mais robustas a outliers e distribuições não
normais, como a mediana e o intervalo interquarti.

A padronização de dados utilizando o RobustScaler é feita da seguinte maneira:

- Calcular a mediana (50 graus percentil) e o IQR (Intervalo interquartil) de cada variável
- Subtrai a mediana de cada valor da variável
- Divide o resultado pelo IQR

Essa transformação garante que os dados estejam centralizados na mediana e que a escala seja ajustada
de acordo com avariabilidade dos dados, tornando-os mais robustos a outliers.
"""

import pandas as pd
from sklearn.preprocessing import RobustScaler

# Dados de exemplo
dados = {
    'idade':[25,30,35,40,45,120],
    'salario':[30000,40000,50000,60000,70000,200000],
    'pontuacao':[50,60,70,80,90,30]
}

df = pd.DataFrame(dados)

# Instancia o RobustScaler
scaler = RobustScaler()

# Gera os dados padronizados
dados_padronizados = scaler.fit_transform(df)
df_padronizados = pd.DataFrame(dados_padronizados, columns=df.columns)

# Dados Originais
print(f"Dados Originais:\n{df}")
print()

# Dados Padronizados
print(f"Dados Padronizados: \n{df_padronizados}")
