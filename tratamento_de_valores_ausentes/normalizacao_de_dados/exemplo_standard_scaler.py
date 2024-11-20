"""
O StandardScaler é uma técnica de pré-processamento usada na análise de dados e no tratamento
de modelos de aprendizado de máquina.

- É usado para padronizar as variáveis, transformando-as para que tenham média zero e desvio
padrão igual a um.

- Técnica usada quando as variáveis apresentam diferentes escalas e distribuições

- Calcula a média e o desvio padrão de cada variável e, em seguida, aplica uma transformação aos dados
substituindo a média e dividindo pelo desvio padrão. Essa transformação garante que as variáveis
tenham média zero e desvio padrão igual a um
"""
import pandas as pd
from sklearn.preprocessing import StandardScaler

from tratamento_de_valores_ausentes.normalizacao_de_dados.exemplo_min_max_scaler import scaler

# Dados de exemplo
dados = {
    'idade':[25,30,35,40,45],
    'salario':[30000,40000,50000,60000,70000],
    'pontuacao':[50,60,70,80,90]
}

df = pd.DataFrame(dados)

# Instanciando o StandardScaler
scaler = StandardScaler()

# Aplicando a transformação de dados
dados_transformados = scaler.fit_transform(df)
df_transformados = pd.DataFrame(dados_transformados, columns=df.columns)

# Dados Originais
print(f"Dados originais:\n{df}")
print()

# Dados Transformados
print(f"Dados padronizados:\n{df_transformados}")
