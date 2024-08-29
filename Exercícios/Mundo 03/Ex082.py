'''Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas gerada'''

valores = []
valores_par = []
valores_impar = []

while True:
    valor = int(input('Informe um valor: '))
    valores.append(valor)
    if valor % 2 == 0:
        valores_par.append(valor)
    else:
        valores_impar.append(valor)
    sair = str(input('Deseja continuar? [S/N]')).upper().strip() [0]
    if sair in 'N':
        break

print('=-'*30)
print(f'A lista com todos os valores é: {valores}.')
print(f'A lista com os valores pares é: {valores_par}.')
print(f'A lista com os valores ímpares é: {valores_impar}.')
print('=-'*30)