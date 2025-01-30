"Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado."

from random import randint as rd

#Criar o dicionário para armazenar os resultados dos jogaroes 
resultados = {}

#Gerar resultados para 4 jogadores 
for jogador in range(1,5):
    resultados[f"Jogador {jogador}"] = rd(1,6)

#Exibir resultados iniciais
print('Resultados Iniciais: ')
for jogador, resultado in resultados.items():
    print(f"{jogador},{resultado}")

    # Ordenar o dicionário com base nos valores (do maior para o menor)
resultados_ordenados = dict(sorted(resultados.items(), key=lambda item: item[1], reverse=True))

# Exibir os resultados ordenados
print("\nClassificação final:")
for posicao, (jogador, resultado) in enumerate(resultados_ordenados.items(), start=1):
    print(f"{posicao}º lugar: {jogador} com {resultado}")
