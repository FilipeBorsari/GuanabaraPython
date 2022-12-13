#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

cidade = str(input('Fale o nome de uma cidade? '))



print ('a Frase começa com Santo?: {}'.format('santo' in cidade.strip().lower()))


#a solução do guanabara foi a seguinte:

# cid = str(input('Em que cidade você nasceu? ')).strip()
# print(cid[:5].upper () == 'SANTO'