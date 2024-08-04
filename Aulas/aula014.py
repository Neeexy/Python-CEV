# Laços - Estrutura de repetição While
n = 1
par = 0
impar = 0
print("Insira '0' para encerrar o programa")
while n != 0:
    n =int(input('Digite um valor: '))
    if n !=0:
        if n %2 == 0:
            par += 1
        else:
            impar += 1
print('Acabou')
print(f'Com {par} pares e {impar} ímpares.')