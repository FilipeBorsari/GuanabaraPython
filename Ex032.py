#Escreva um programa que leia a velocidade de um carro
#Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
#A multa vai custar R$ 7,00 por cada Km acima do limite

vel = float(input('Qual a velocidade do carro (KM/h)? '))

if vel > 80:
    multa = (vel-80)*7
    print ('Você foi multado em: R$ {:.2f}'.format(multa))
else:
    print ('Você está dentro da velocidade permitida! ')