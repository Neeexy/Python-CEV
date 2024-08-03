#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta pinta uma área de 2m^2.
largura = int(input('Informe a largura da parede em metros:'))
altura = int(input('Informe a altura da parede em metros:'))

area = altura*largura
tinta = area/2

print(f'Você terá uma área de {area} metros, e precisará de {tinta} litros de tinta para pintar tudo. Boa sorte')