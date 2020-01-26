"""
REDUCE

OBS: A partir de Python3+ a função recude() nãi é mais uma função integrada (built-in), agora temos que importar e
utilizar essa função a partir do móculo 'functools'

GUIDO VAN ROSSUM: Utilize a função reduce() se você realmente percisar dela. Em todo caso, 99% um loop for é mais
legível

Entendendo o reduce()
Imagine que tem uma coleção de dados:
dados = [a1, a2, a3, ..., an]

E você tem uma função que recebe dois parâmetros

def funcao(x, y):
    return x * y

Assim como map() e filter() a função reduce() recebe dois parâmetros: a função e o iterável.

reduce(funcao, dados)

A função reduce() funciona da seguinte forma:
    Passo 1: res1 = f(a1, a2) aplica a função nos dois primeiros elementos e guarda os resultados
    Passo 2: res2 = f(res1, a3) aplica o função, passando o resultado do passo1 mais o terceiro elemento, e guarda o
resultado, isso ocorre até o final, até an.

Isso é repetido até o final.
    Passo 3: res3 = f(res2, a4)
    .
    .
    Passo n: resm = f(resn, an)

Alternativamente podemos ver a função reduce() como:
funcao(funcao(funcao(a1, a2), a3), a4), ...), an)
"""
from functools import reduce

dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 29]


# Precisamos de uma função que receba dois parâmetros
multi = lambda x, y: x * y

res = reduce(multi, dados)
print(res)

# Com loop
res = 1
for x in dados:
    res = res * x

print(res)
