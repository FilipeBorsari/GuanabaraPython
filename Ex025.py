# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas maiúsculas
# O nome com todas minúsculas
# Quantas letras ao todo sem considerar espaços
# quantas letras tem o primeiro nome
nome = str(input('qual seu nome? ')).strip() #esse strip ja elimina possíveis espaçps inúteis
tamanho = len(nome) - nome.count(' ') #Conta o tamanho do nome 'menos' os espaços
lista = nome.split()
pnome = len(lista[0])
print ('Seu nome em maíusculo é: {} '.format(nome.upper()))
print ('Seu nome em minúsculo é: {}'.format(nome.lower()))
print('Seu nome Possui ao todo {} letras'.format(tamanho))
print ('Seu primeiro nome é {[0]} e tem {} Letras '.format(lista,pnome))


#Solução do Guanabara:

print('\nAnalisando seu nome...')
print ('Seu nome em maiúsculas é {} '.format(nome.upper()))
print ('Seu nome em minúsculas é {} '.format(nome.lower()))
print ('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print ('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

