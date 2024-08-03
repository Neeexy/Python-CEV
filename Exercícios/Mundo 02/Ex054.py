'''Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''

#Passo 1 - Requisitar ano de nascimento
#Passo 2 - Calcular a idade com base no ano atual
#Passo 3 - Contar número de maiores e menores
#Passo 4 - Exibir o resultado

from datetime import date

#--------------
year = date.today().year
minor = 0
major = 0
for p in range(1, 8):
        name = str(input(f'Informe o nome da {p}º pessoa: '))
        birth = int(input(f'Informe o ano de nascimeto de {name}: '))
        age = year - birth
        if age < 18:
                minor.append(name)
        else:
                major.append(name)
print(f'\nExistem {len(minor)} menores de idade e {len(major)} maiores de idade!')

print(f'''Lista de maiores:
        {major}\n''')
print(f'''Lista de menores: 
        {minor}''')
#-------------