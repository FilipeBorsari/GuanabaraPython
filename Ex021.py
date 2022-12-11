#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
from math import sin,cos,tan,radians


ang = int(input('Escolha um angulo qualquer: '))
#o valor recebido está em graus, a função precisa do valor em radianos, pra isso usarei a função radians
seno = sin(radians(ang))
cos = cos(radians(ang))
tg = tan(radians(ang))

print('O valor do Seno é: {:.2f},\nDo Cosseno é: {:.2f}\nDa Tangente é: {:.2f}'.format(seno,cos,tg))