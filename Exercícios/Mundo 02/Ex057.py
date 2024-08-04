'''Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.'''
sexo = str(input('Informe seu sexo [M/F]: ')).upper()[0].strip()
while sexo not in 'MfmF':
    sexo = str(input('Dados inválidos. Por favor, informe seus dados corretamente: ')).upper()[0].strip()
print(f'Sexo {sexo} registrado com sucesso!')