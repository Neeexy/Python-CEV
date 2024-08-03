#Condicionais
'''nome= str(input('Qual é seu nome? '))
if nome== 'Gustavo':
    print('Que nome lindo')
else:
    print('Seu nome é tão normal.')
print(f"Bom dia, {nome}!")'''

nota1=float(input('Digite a 1º nota: '))
nota2=float(input('Digite a 2º nota: '))
média = (nota1 + nota2) /2 
print(f'A sua média foi: {média:.1f}.')
'''if média >=6:
    print(f'Sua média foi boa, parabéns.')
else:
    print(f'Sua média foi ruim, estude mais.')'''
print('Parabéns' if média >=6 else 'Estude mais')
