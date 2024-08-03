'''Exercício Python 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos'''

#Passo 1 - Recolher as informações (Nome e Peso[kg])
#Passo 2 - Analisar informações
#Passo 3 - Exibir resultados

#----------
dados = {}
for i in range (5):
    nome = str(input(f'Informe o nome da {i+1}º pessoa: '))
    peso = float(input(f'Informe o peso de {nome} (KG): '))
    dados[nome] = peso # Adciona a chave 'nome' ao dicionário com o valor 'peso'.
maior_peso = max(dados, key=dados.get) #Verfica maior peso
menor_peso = min(dados, key=dados.get) #Verfica menor peso

maiores_pesos = []
menores_pesos = []

for nome, peso in dados.items():
    if peso == maior_peso: #Compara o peso para ver se ele é o maior, se for, é adcionado à lista. (Para casos onde existam pessoas com pesos iguais)
        maiores_pesos.append(nome)
    elif peso == menor_peso: #Compara o peso para ver se ele é o menor, se for, é adcionado à lista. (Para casos onde existam pessoas com pesos iguais)
        menores_pesos.append(nome)

if maiores_pesos == 1 and menores_pesos == 1:
    print(f'''
    |A pessoa com maior peso é: {', '.join(maiores_pesos)}, pesando: {dados[maior_peso]},
    e a pessoa com o menor peso é: {', '.join(menores_pesos)}, pesando: {dados[menor_peso]}|
''')
elif maiores_pesos > 1 and menores_pesos == 1:
    print(f'''
    |As pessoas com os maiores pessos são: {', '.join(maiores_pesos)}, pesando: {dados[maior_peso]}
     e a pesso com o menor peso é: {', '.join(menores_pesos)}, pesando: {dados[menor_peso]}|
''')
elif maiores_pesos ==1 and menores_pesos > 1:
    print(f'''
    |A pessoa com o maior peso é: {', '.join(maiores_pesos)}, pesando: {dados[maior_peso]}
     e as pessoas com os menores pesos são: {', '.join(menores_pesos)}, pesando: {dados[menor_peso]}|
''')
else:
    print(f'''
    |As pessoas com maiores pesos são: {', '.join(maiores_pesos)}, pesando: {dados[maior_peso]}
     e as pessoas com os menores pesos são: {', '.join(menores_pesos)}, pesando: {dados[menor_peso]}|
''')