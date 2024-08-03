'''Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''
# Passo 1 - Recolher informações (Nome, Idade, Sexo)
# Passo 2 - Analisar informações
# Passo 3 - Exibir informações Organizadamente

dados = {}
idades = 0
Fem = 0
Fem_20 = 0
for i in range(7):
    print(f'---- {i+1}º Pessoa ----')
    nome = str(input(f'Informe o nome da {i+1}º Pessoa: ')).strip()
    idade = int(input(f'Informe a idade de {nome}: '))
    sexo = str(input(f'Informe o sexo de {nome} (F/M): ')).upper()
    if sexo == 'F':
        Fem += 1
        if idade < 20:
            Fem_20 += 1
    dados[nome] = {'Idade': idade, 'Sexo': sexo}

for nome, info in dados.items():
    idades += info['Idade']
media = idades / len(dados)

homens = {nome: info for nome, info in dados.items() if info['Sexo'] == 'M'}
if homens:
    mais_velho = max(homens, key= lambda x: homens[x]['Idade'])
else:
    mais_velho = None
print(f'''
    - A média de idade do grupo é de {media:.2f} anos.
    - O Grupo tem um total de {Fem_20} mulheres com menos de 20 anos.
''')
if mais_velho:
    print(f'''
    - O homem mais velho do grupo é o {mais_velho}, com {dados[mais_velho]['Idade']} anos.
''')
else:
    print('''- Não há homens no grupo.''')