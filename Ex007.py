n1 = int (input('Um valor: '))
n2 = int (input('Outro valor: '))

soma = n1+n2
mult = n1*n2
div = n1/2
divint = n1//n2
sobradiv = n1%n2
pot = n1**n2

print ('a soma é {}, a multiplicação é {}, a divisão é {} a divisão inteira é {}'.format(soma,mult,div,divint), end=' ')
print ('e a potencia é {}'.format (pot))
