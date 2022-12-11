#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

preco = float(input('Qual o valor do produto? '))

desconto = (preco/100)*5
novopreco = preco-desconto


print('o valor do produto com 5% de desconto é {}!'.format(novopreco))
