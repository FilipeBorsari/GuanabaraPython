#Digitar um programa que receba uma informação e exiba tudo sobre ela
data1 = input ('Digite alguma coisa: ')

print('A informação digitada é um: {}'.format (type (data1)))
print ('Ela é um alpha númerico: {}'.format (data1.isalnum()))
print ('Ela é um alpha: {}'.format (data1.isalpha()))
print ('Ela é um digito: {}'.format (data1.isdigit()))
print ('Ela está digitada em minusculo: {}'.format (data1.islower()))





