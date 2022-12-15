#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
#para salários superiores a 1250, calcule um aumento de 10%
#Para os inferiores ou iguais, o aumento é de 15%

salario = float(input('Qual o salário? '))

if salario > 1250:
    salario = salario + 0.10*salario
else:
    salario = salario + 0.15*salario
print ('O novo salário será de {}'.format(salario))