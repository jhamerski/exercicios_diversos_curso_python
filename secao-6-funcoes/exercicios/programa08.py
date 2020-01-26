"""
Faça uma função de numeros inteiros que retorne a soma entre dois números. OBS: Os números informados não devem ser
inclusos.
"""


def soma(p, u):
    total = 0
    for i in range(p + 1, u):
        total = total + i
    return total


print(soma(1, 10))
