"""
ASSERTIONS (CHECAGENS/QUESTIONAMENTOS)

Em Python utilizamos a palavra 'assert' para realizar afirmações utilizadas nos testes

Utilizamos o 'assert' em uma expressão que queremos checar se é válida ou não. Se a expressão for verdadeira o assert
retorna None e caso seja falsa, levanta um erro do tipo AssertionError

OBS: Nós podemos especificar, opcionalmente, um segundo argumento ou mesmo uma mensagem de erro personalizada

A palavra 'assert' pode ser utilizada em qualquer função ou código nosso... não precisa ser exclusivamente nos testes

# ALERTA: Cuidado ao utilizar o 'assert'

Se o programa for executado com o comando(flag)
 -O, nenhum assertion será válidado. Ou seja, todas as suas validações são
perdidas
"""


def soma_numeros_positivos(a, b):
    assert a > 0 and b > 0, 'Ambos números precisam ser positivos'
    return a + b


print(soma_numeros_positivos(1, 10))
# print(soma_numeros_positivos(1, -10))  AssertionError


def comer_fast_food(comida):
    assert comida in [
        'pizza',
        'sorvete',
        'doces',
        'batata-frita',
        'cachorro-quente'
    ], 'A comida precisa ser fast food'
    return f'Eu estou comendo {comida}!'


comida = input('Informe a comida: ')
print(comer_fast_food(comida))

# ALERTA: Cuidado ao utilizar o 'assert'
