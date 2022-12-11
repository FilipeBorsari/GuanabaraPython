# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas minúsculas
# Quantas letras sem considerar espaços
# quantas letras tem o primeiro nome


nome = str(input('qual seu nome? '))
nomestrip = nome.strip()
nomesplit = nome.split()


print ('o nome com letras minuscula: {}'.format(nome.lower()))
print ('Possui {} letras '.format(len(nomestrip)))
print (len(nome.strip()))