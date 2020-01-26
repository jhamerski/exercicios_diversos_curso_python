"""
*ARGS

- O *args é um parâmetro como outro qualquer. Isso significa que você poderá chamar de qualquer coisa, desde que comece
com arterisco.
Exemplo:
    *xis

    Mas por convenção, utilizamos *args para defini-lo.

O que é *args?
Ele coloca os valores extras informados por parâmetros em uma tupla. Então desde já lembre-se que tuplas são imutáveis
"""


# Entendendo o *args
def soma_todos_numeros(*args):
    return sum(args)


print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(1, 2, 3, 4,))
print(soma_todos_numeros(243, 345, 4))


def verifica_info(*args):
    if 'Jonas' in args and 'Hamerski' in args:
        return f'Bem vindo Jonas Hamerski'
    return 'Não tenho certeza quem é você!'


print(verifica_info())
print(verifica_info(1, True, 2.5, 'Jonas'))
print(verifica_info(123.00, 'Jonas', 'Hamerski'))
print(verifica_info(False, 'Hamerski', 'Jonas', True))


def soma_todos(*args):
    return sum(args)


print(soma_todos())
print(soma_todos(3, 4, 5, 6))

numeros = [1, 2, 3, 4, 5, 6, 7]

# Desempacotador
print(soma_todos(*numeros))  # O * serve para que informar ao Python que estamos passando uma Collection de dados
