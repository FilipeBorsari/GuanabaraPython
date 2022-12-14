#Escreva um programa que faça o computador "pensar" em um número inteiro
#entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido
#O programa deverá escrever na tela se o usuário venceu ou perdeu

import random

num = random.randint(0, 5)

choose = int(input('Tente adivinhar o número que pensei de 0 a 5: '))

if choose == num:
    print('Parabéns, você acertou! ')

else:
    print('Você errou! ')