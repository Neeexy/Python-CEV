# Aula - 15 Interrompendo Estruturas de Repetição While
'''num = s =0

while True:
    num = int(input('Digite um número: '))
    leave = str(input('Deseja adicionar outro número? [S/N] ')).upper().strip() [0]
    s += num
    if leave in 'N':
        break
    else:
        continue
print(f'A soma vale : {s}')'''

#Segunda versão

num = sum = cont = 0

while True:
    num = str(input('Digite um número ["Sair" para sair]: ')).upper()

    if num == 'SAIR':
        break
    
    if not num.isdigit():
        print('Entrada inválida, tente novamente.') # Se o usuário digitar  qualquer palavra que não seja 'Sair', o código
        continue
    
    num = int(num)
    sum += num
    cont += 1
print()
print('=-='*20)
print(f' Foram inseridos: {cont} valores e a soma entre eles é: {sum}.')
print('=-='*20)