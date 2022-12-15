#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
#se elas podem ou não formar um triângulo.
print ('-='*20)
print ('Bem vindo ao analisador de Triângulos')
print ('-='*20)


r1 = float(input('Informe o comprimento da Reta 1 '))
r2 = float(input('Informe o comprimento da Reta 2 '))
r3 = float(input('Informe o comprimento da Reta 3 '))

#para um triangulo existir, a soma de 2 lados deve ser menor que o 3



if r1+r2>r3 and r2+r3>r1 and r1+r3>r2 :
    print('Essas retas podem formar um triângulo')
else:
    print ('Essas retas não podem formar um triângulo')