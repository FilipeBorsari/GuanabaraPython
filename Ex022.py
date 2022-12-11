#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido
from random import choice

a1 = str(input('Qual nome do aluno 1? '))
a2 = str(input('E do aluno 2? '))
a3 = str(input('E do aluno 3? '))
a4 = str(input('E do aluno 4? '))

print('o aluno sorteado foi {} '.format(choice([a1,a2,a3,a4])))

#a solução do professor foi criando uma lista (lista = [a1,a2,a3,a4]) e dando choice(lista)
