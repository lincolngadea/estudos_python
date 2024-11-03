import matplotlib.pyplot as plt

anos = [2010, 2011, 2012, 2013, 2014, 2015, 2016]
variavel1 = [10, 20, 30, 25, 135, 40, 50]
variavel2 = [20, 15, 25, 30, 40, 35, 45]
variavel3 = [5, 10, 15, 20, 25, 30, 35]

# Criando uma figura e os eixos
fig, ax = plt.subplots()

# Plotando as áreas
ax.stackplot(
    anos,
    variavel1,
    variavel2,
    variavel3,
    labels= [
        'Variável 01',
        'Variável 02',
        'Variável 03'
    ],
    colors=[
        '#FF7F50',
        '#6A5ACD',
        '#FFD700'
    ],
    alpha=0.7
)

# Personalização do gráfico
ax.set_title('Gráfico de área - Variáveis ao longo do tempo')
ax.set_xlabel('Anos')
ax.set_ylabel('Valores')

# Personaliza a legenda e a grade
ax.legend(loc = 'upper left')

# Exibe o gráfico
plt.show()