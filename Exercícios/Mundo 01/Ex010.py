#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.  Considere U$1=R$3.27

saldo = float(input('Digite seu saldo bancario: R$'))
valor_dolar = 5.49
rs_dol= saldo/valor_dolar
print (f'Você consegue comprar ${rs_dol:.2} com seu saldo atual. FAZUELY')