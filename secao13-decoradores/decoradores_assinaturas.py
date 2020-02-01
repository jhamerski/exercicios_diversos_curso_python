"""
DECORATORS COM DIFERENTES ASSINATURAS

Para resolver o TypeError: aumentar() takes 1 positional argument but 2 were given, utilizamos um padrão de projeto
chamado DECORATOR PATTERN

A ASSINATURA DE UMA FUNÇÃO é representada pelo seu retorno, nome e parâmetros de entrada.

"""


# Relembrando
def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou o/a {nome}'


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor.'


# Testando
print(saudacao('Jonas'))

# print(ordenar('churrasco', 'batata frita'))


# Refatorando com DECORATOR PATTERN
def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou o/a {nome}'


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor.'


print(ordenar('churrasco', 'batata frita'))


@gritar
def lol():
    return 'lol'


print(lol())

# OBS: Vale lembrar que podemos utilizar parâmetros nomeados
print(ordenar(acompanhamento='batata frita', principal='picanha'))


# Decorator com argumentos
def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto! Primeiro agumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna


@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)


@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2


# Testando
print(soma_dez(10, 12))  # 22
print(soma_dez(1, 21))

print(comida_favorita('pizza', 'churrasco'))
print(comida_favorita('churrasco', 'pizza'))
