"""
PRESERVANDO METADATAS COM WRAPS

Metadados (METADATAS) -> São dados intrísecos em arquivos.

WRAPS -> São funções que envolvem elementos com diversas finalidades.


# Problema
def ver_log(funcao):
    def logar(*args, **kwargs):
        ### Eu sou a função (logar), dentro de outra ###
        print(f'Você está chamando a função: {funcao.__name__}')
        print(f'Aqui sobre a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    ### Soma dois números. ###
    return a + b


print(soma(10, 30))

print(soma.__name__)
print(soma.__doc__ )
"""
from functools import wraps


# Problema (RESOLUÇÃO)
def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """Eu sou a função (logar), dentro de outra"""
        print(f'Você está chamando a função: {funcao.__name__}')
        print(f'Aqui sobre a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """Soma dois números."""
    return a + b


print(soma(10, 30))

print(soma.__name__)
print(soma.__doc__ )


