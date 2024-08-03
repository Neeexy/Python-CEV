#Crie um algoritimo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

numero= float(input(f'Digite um número aleatório: '))
dobro= numero*2
triplo= numero*3
raiz= numero**(1/2)
print(f'{"Aqui estão os resultados das operações"}')
print(f'Dobro do número: |{dobro:-^10}|')
print(f'Triplo do número: |{triplo:-^10}|')
print(f'Raiz do número: |{raiz:-^10.3f}|')