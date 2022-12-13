#Faça um programa que leia o nome completo de uma pessoa, mostrando
#em seguida o primeiro e o último nome separadamente
# Ex: Ana Maria de Souza = primeiro = Ana // último = Souza

nome = str(input('Qual seu nome completo? '))

divide = nome.split()

print ('Seu primeiro nome é: {}'.format(divide[0]))
print ('Seu último nome é: {}'.format(divide[-1]))