import matplotlib.pyplot as plt
import matplotlib.cm as cm

categorias = ['A','B','C','D']
valores = [30,25,20,15]

# Configurações de cores
cores_pastel = cm.get_cmap('Pastel1')

# Criação de gráfico de pizza com cor pastel
plt.pie(
    valores,
    labels=categorias,
    colors=cores_pastel(range(len(categorias))),
    autopct='%1.1f%%'
)

# Personalizaçao do gráfico
plt.title('Distribuição por Categoria')

# Exibe o gráfico
plt.show()
