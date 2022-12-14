#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO
import calendar

ano = int(input('Escolha um ano qualquer: '))

if calendar.isleap(ano): #função isleap verifica se o ano é bissexto
    print ('O ano {} é Bissexto'.format(ano))

else:
    print ('O ano {} não é bissexto'.format(ano))