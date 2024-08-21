resposta = 'S'
soma = quant = média = 0

while resposta in 'Ss':
    numeros = int(input('Digite um número: '))
    soma += numeros
    quant += 1
    if quant == 1:
        maior = menor = numeros
    else:
        if numeros > maior:
            maior = numeros
        if numeros < menor:
            menor = numeros
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip() [0]
média = soma / quant
print(f'Você digitou {quant} números e a média foi {média}.')
print(f'O maior valor foi {maior} e o menor foi {menor}')
print('Fim')
