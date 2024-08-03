''' Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida'''

print('Vamos verificar seu índicie de massa corpórea?\n')
peso=float(input('Informe seu peso em Kg: \n'))
altura=float(input('Informe sua altura em M: '))
imc= peso /(altura**2)

if imc <= 18.5:
    print(F'\nSeu IMC é de {imc:.2f}, você está abaixo do peso ideal. ')
elif imc <= 25:
    print(F'\nSeu IMC é de {imc:.2f}, você está no peso ideal. ')
elif imc <=30:
    print(F'\nSeu IMC é de {imc:.2f}, você está com sobrepeso. ')
elif imc <=40:
    print(F'\nSeu IMC é de {imc:.2f}, você está com obesidade. ')
else:
        print(F'\nSeu IMC é de {imc:.2f}, você está com obesidade mórbida, parabéns ')
