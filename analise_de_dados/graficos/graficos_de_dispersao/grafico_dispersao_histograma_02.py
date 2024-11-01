import matplotlib.pyplot as plt

# Imagine que você é um professor e aplicou uma prova para uma turma de 100 alunos.
# Agora, você quer entender como as notas estão distribuídas,
# ou seja, quantos alunos tiraram notas baixas, médias ou altas

# Notas dos alunos
notas = [55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]

# Criar o histograma
plt.hist(notas, bins=10, edgecolor='black')

# Adicionar título e rótulos aos eixos
plt.title('Distribuição de Notas dos Alunos')
plt.xlabel('Notas')
plt.ylabel('Número de Alunos')

# Mostrar o gráfico
plt.show()