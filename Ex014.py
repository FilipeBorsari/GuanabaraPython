#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área
#e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²

largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura? '))

mq = largura * altura

tinta = mq/2

print('serão necessários {} litros de tinta para pintar essa parede '.format(tinta))
