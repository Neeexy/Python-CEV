'''Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo. '''

numero = 0
n = 10
while True:
    numero = str(input('Insira o número que você quer a tabuada ["Sair" para sair]: ')).upper()

    if numero == 'SAIR':
        break
    if not numero.isdigit():
        print('Entrada inválida, tente novamente.')
    numero = int(numero)

    if numero < 0:
        print('\nPrograma interrompido! Inserção indisponível.')
        break
    for n in range (n+1):
        resultado = numero * n
        print(f"|{numero} x {n}| = | {resultado} |")

if numero == 'SAIR' or numero  >0:
    print('\nPrograma Encerrado!')