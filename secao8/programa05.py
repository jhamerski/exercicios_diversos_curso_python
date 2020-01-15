"""
Faça uma função que receba 03 números inteiros como parâmetros, representado por horas, minutos e segundos e converta-os
em segundos.
"""


def hms(h, m, s):
    return (h * 3600) + (m * 60) + s


print(hms(1, 1, 0))
