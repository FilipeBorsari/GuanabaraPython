#Criar um programa que converta cº em fº

celsius = float(input('Qual a temperatura em CELSIUS? ' ))

f = (9 * celsius / 5) + 32

print('A temperatura de {}ºC corresponde a {}ºF'.format(celsius,f))
