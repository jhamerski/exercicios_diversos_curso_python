"""
Faça uma função determinada DESENHALINHA. Ela deve desenhar uma linha na tela usando vários símbolos de iguail. Exemplo
(=======). A função recebe por parâmetro quantos sinais de iguais ela deverá mostrar.
"""


def desenha_lina(x):
    return x * '= '


qtd = (int(input(f'Informe uma quantidade que deveja ver: ')))
print(desenha_lina(qtd))
