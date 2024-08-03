'''Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.'''
#Passo 1 - Inserir números
#Passo 2 - Verificar se são pares
#Passo 3 - Somar e imprimir

soma = 0
counter = 0
numbers = []
p_pos = []
i_pos = []
for n in range(1,7):
    number = int(input(f'Digite o {n}º valor: '))
    numbers.append(number)
    if number % 2 == 0:
        soma += number
        counter += 1
        p_pos.append(n)
    else:
        i_pos.append(n)
if counter > 2:        
    print(f"Você informou {counter} números pares e a soma entre eles foi: {soma}")
    print(f'As posições dos números pares foram:', end=' ')
    print(f','.join([f"{pos}º" for pos in p_pos]))
elif counter == 1:
    print(f"Você informou {counter} número par e não há possibilidade de soma.")
    print(f'A posição do número par foi: {p_pos[0]}º')
else:    
    print(f"Você não informou nenhum número par e não há possibilidade de soma.")
if i_pos:
    print(f'Os outros números inseridos são ímpares e estão nas posições: ', end=' ')
    print(f','.join([f"{pos}º" for pos in i_pos]))


#------------------------#
