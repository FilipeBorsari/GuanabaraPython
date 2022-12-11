#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salario = int(input('Qual o seu salário? '))

aumento = salario+(salario*15/100)

print ('com 15% de aumento seu salário passará a ser: R$ {} '.format(aumento))

