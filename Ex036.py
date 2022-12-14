#Faça um programa que leia três números e mostre qual é o maior e qual é o menor

num1 = int(input('Escolha o número 1: '))
num2 = int(input('Escolha o número 2: '))
num3 = int(input('Escolha o número 3: '))


if num1 > num2 and num1 > num3:
    print ('o maior é {}'.format(num1))
if num2 > num1 and num2 > num3:
    print ('o maior é {} '.format(num2))
if num3 > num2 and num3 > num1:
    print ('o maior é {} '.format(num3))
if num1 < num2 and num1 < num3:
    print ('o menor é {}'.format(num1))
if num2 < num1 and num2 < num3:
    print ('o menor é {} '.format(num2))
if num3 < num2 and num3 < num1:
    print ('o menor é {} '.format(num3))
