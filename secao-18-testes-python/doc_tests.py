"""
DOCTESTS

Doctest são testes que colocamos na DocString das funções/métodos Python

def soma(a, b):
    # soma os numeros a e b

    #soma(1, 2)
    #3

    #soma(4, 6)
    #10
    #
    # return a + b

print(soma(3, 4))


Para rodar um teste do Doctest:
    - python -m doctest -v 'nome_do_módulo'.py
Saída:

Trying:
    soma(1, 2)
Expecting:
    3
ok
1 items had no tests:
    doctests
1 items passed all tests:
    1 tests in doctests.soma
1 tests in 2 items.
1 passed and 0 faileds.
Test passed .

"""


# Aplicando o TDD
def duplicar(valores):
    """duplica os valores da lista

    >>>duplicar([1, 2, 3, 4])
    [2, 4, 6, 8]

    >>>duplicar([])
    []

    >>>duplicar(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']

    >>>duplicar([True, None])
    Traceback (trace recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and  'NoneType'
    """
    return [2 * elemento for elemento in valores]


# Dentro do Doctest o Python não reconhece String com aspas duplas"", precisa ser aspas simples''
def fala_oi():
    """Fala oi

    >>>fala_oi()
    'oi'
    """
    return "oi"




