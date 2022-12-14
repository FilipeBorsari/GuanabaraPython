#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR


num = int(input('Digite Um Número Qualquer: '))
resto = num % 2

if resto == 0:
    print('O número escolhido é Par')

else:
    print('O número escolhido é Ímpar ')