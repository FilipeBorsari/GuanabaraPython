#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retânguloi, calcule e mostre o comprimento da hipotenusa

from math import hypot #como só irei utilizar a função hypot, não há necessidade de importar math inteira


cat = float(input('Qual o valor do cateto adjacente? '))
catop = float(input('Qual o valor do cateto oposto? '))

print('A hipotenusa equivale a {:.2f} '.format(hypot(cat,catop)))

#obs: também poderia criar uma nova variável para receber o valor da função hypot e depois exibir ela
