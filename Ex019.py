#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira
import math #na solução data pelo professor, podemos importar somente a função trunc, deixando o programa mais leve

num = float(input('Escolha um numero: '))


#minha solução foi:
print ('\nArredondando {} para cima temos {}'.format(num, math.ceil(num)))
print ('E arredondando para baixo temos {}'.format(math.floor(num)))

#essa foi a solução criada pelo professor
print('A porção inteira de {} é: {}'.format(num,math.trunc(num))) #função trunc pega a porção inteira de um num float
