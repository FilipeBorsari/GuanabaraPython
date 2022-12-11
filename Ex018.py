#exercício função import = exibir a raiz quadrada usando a função sqrt da biblioteca math
import math #para importar somente algumas funções podemos usar "from math import xxx,xxx
num = int(input('Digite um número: '))
raiz = math.sqrt(num)

print('a raiz de {} é {}'.format(num,math.ceil(raiz))) #ceil = arredonda para cima
