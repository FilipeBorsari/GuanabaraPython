#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar
#considere US$ 1,00 = R$ 3,27

wallet = float(input('quantos reais você tem na sua carteira? R$ '))

conv = wallet * 3.27
comp = wallet / 3.27
print ('esse valor equivale em dolar US$: {:.2f} '.format(conv))
print ('voce poderia comprar US$ {:.2f} '.format(comp))

