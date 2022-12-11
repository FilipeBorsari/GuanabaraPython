#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

valor = float(input('Insira uma medida em metros: '))

cm = valor*100
mm = valor*1000

print('essa medida em cm é {} e em mm é {}'.format(cm,mm))
