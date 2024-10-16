import numpy as np

# O projeto consiste em uma loja que realiza vendas durante a semana e será calculado valores das vendas
# conforme os exemplos do projeto

# Matriz correspondente aos dias da semana(linha) e quantidade de vendas (Colunas)
vendas_semanais = np.array(
    [
        [12, 34, 56, 7],
        [23, 4, 55, 6],
        [22, 3, 44, 56],
        [12, 34, 53, 20],
        [78, 34, 5, 32]
    ]
)

print(f"Vendas da Semana: \n{vendas_semanais}")

#Total de vendas em cada dia da semana
total_venda = np.sum(vendas_semanais, axis=1)
print(f"Vendas Totais por dia da semana: {total_venda}")

#Total de vendas semanais
vendas_dia = np.sum(vendas_semanais, axis=0)
print(f"Vendas de cada produto na semana: {vendas_dia}")

#Média de vendas semanais
media_semanal = np.mean(vendas_semanais, axis=0)
print(f"Média de vendas na semana: {media_semanal}")

#Média de vendas diárias
media_dia = np.mean(vendas_semanais, axis=1)
print(f"Média de produtos vendidos no dia: {media_dia}")

#Produto com menor variação nas vendas ao longo da semana
desvio_padrao = np.std(vendas_semanais, axis=0)
variacao_minima = np.argmin(desvio_padrao)

print(f"Variação de Vendas na semana: {desvio_padrao}")
print(f"O Produto {variacao_minima +1} está com menor variação de Vendas:")

#Produto que vendeu mais e menos na semana

maior_venda = np.argmax(np.sum(vendas_semanais,axis=0))
menor_venda = np.argmin(np.sum(vendas_semanais,axis=0))

print(f"O Produto {maior_venda + 1} Teve a maior venda da semana")
print(f"O Produto {menor_venda + 1} teve a menor venda da semana")