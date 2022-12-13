#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

nome = str(input('Qual seu nome completo? '))

print ('O nome possui SILVA: {}'.format('silva' in nome.lower()))