"""
Faça uma função que receba um número inteiro positivo e retorne seu fatorial
"""


def fatorial(x):
    if x == 1:
        return x
    else:
        return x * fatorial(x - 1)


print(fatorial(5))
