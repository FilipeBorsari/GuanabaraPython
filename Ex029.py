#Faça um programa que leia uma frase pelo teclado e mostre:
# quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a última vez.

frase = str(input('Digite uma frase ').strip())

letra_a = frase.lower().count('a') #primeiro converto para lowcase, pra garantir que irei contar todos os 'a'.
primeiro = frase.lower().find('a')+1 #irá encontrar a primeira vez que o A aparece e desconsiderando indice 0
ultimo = frase.lower().rfind('a')+1 #irá encontrar a primeira vez que o A aparece da direita pra esquerda, ou seja, última vez

print ('A letra A aparece {} vezes, \nA primeira vez no índice {} \nA última no índice {}'.format(letra_a , primeiro , ultimo))