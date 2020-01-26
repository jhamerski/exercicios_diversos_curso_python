"""
**KWARGS

- O **kwargs é um parâmetro como outro qualquer. Isso significa que você poderá chamar de qualquer coisa, desde que
comece com duplo arterisco.
Exemplo:
    *xis

    Mas por convenção, utilizamos **kwargs para defini-lo.

O **kwargs coloca os valores em uma tupla, o **kwargs exige que utilizemos parâmetros nomeados, e transforma esses
parâmetros extras em um dicionário

OBS: Os parâmetros *args e **kwargs não são obrigatórios.

Temos que SEGUIR ESSA ORDEM
- Parâmetros obrigatórios.
- *args
- Parâmetros default (não obrigatórios).
- **kwargs
"""
from distutils.command.config import config


def cores_favorritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}!')


cores_favorritas(marcos='verde', julia='rosa', jonas='vermelha', carlos='azul')


# Exemplo mais complexo
def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimeto Pythônico Geek!'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} 'Geek'"
    return 'Não tenho certeza quem você é!'


print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='Especial'))


# Vários tipos de parâmetros na mesma função
def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos.')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)


minha_funcao(8, 'Julia')
minha_funcao(32, 'Jonas', 4, 5, solteiro=True)
minha_funcao(34, 'Felipe', eu='Não', você='Vai')
minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True)


# Entendendo a importância das ordens do parâmetros
def mostra_info(a, b, *args, instrutor='Geek', **kwargs):
    return[a, b, args, instrutor, kwargs]
"""
a = 1
b = 2
args = 3
instrutor = 'Geek'
kwargs = {'sobrenome': 'University', 'cargo': 'Instrutor'}
"""

print(mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))


# Desempacotar
def mostrar_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'Jonas', 'sobrenome': 'Hamerski'}

print(mostrar_nomes(**nomes))


def soma_multiplos(a, b, c):
    print(a + b + c)


lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}

dicionario = dict(a=1, b=2, c=3)  # Os nomes das chaves, devem ser o mesmo dos parâmetros da função

soma_multiplos(*lista)
soma_multiplos(*tupla)
soma_multiplos(*conjunto)

soma_multiplos(**dicionario)


