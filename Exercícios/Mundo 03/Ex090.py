'''Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.'''

ficha = {}

ficha['nome'] = input('Nome: ')
ficha['media'] = float(input('Média: '))

md = ficha['media']
print('=-'*30)
print(f'''
        - Nome do aluno : {ficha['nome']}
        - Média de {ficha['nome']} : {ficha["media"]}
''',end='')
if  md >=6 :
    print(f'''        - Situação de {ficha['nome']} - Aprovado
''')
elif 4 <= md <5:
    print(f'''        - Situação de {ficha['nome']} - Recuperação
''')
else:
    print(f'''        - Situação de {ficha['nome']} - Reprovado
''')
print('=-'*30)