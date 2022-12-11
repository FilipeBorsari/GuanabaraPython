#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

num = int(input ('Insira um número: '))

dobro = num*2
triplo = num*3
raiz = num ** (1/2)

print('O dobro é {}, o triplo {} e a raiz {.2f}'.format(dobro,triplo,raiz))

#.2f serve para escolher as casas decimais