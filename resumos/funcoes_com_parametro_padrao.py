"""
FUNÇÕES COM PARÂMETRO PADRÃO - (DEFAULT PARAMTERS)

Funções onde a passagem de parâmetro seja opcional
"""
# Passagem de parâmetro opcional
print('Jonas Hamerski')
print()


# Passagem de parâmetro obrigatório
def quadrado(numero):
    return numero ** 2


print(quadrado(4))
# print(quadrado())


# Passagem por parâmetro opcional (Quando não for passado o segundo parâmetro, nesse caso ele recebe valor: 2)
def exponencial(numero, potencia=2):
    return numero ** potencia


print(exponencial(2, 8))
print(exponencial(9))  # Nesse caso o agumento "9", está sendo atribuido ao parâmetro "número"

# OBS: Os parâmetros com valor Default (padrão) DEVEM sempre estar ao final da declaração
"""
Errado
def teste(num=2, potencia):
    return num ** potencia
    
Correto
def teste(potencia, num=2):
    return num ** potencia
"""


# Exemplo mais complexo
def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem-vindo Geek'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor!'
    return f'Olá {nome}!'


print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(True))
print(mostra_informacao('Jonas'))
print(mostra_informacao(nome='Hamerski'))

"""
Por quê utilizar parâmetros com valores Default?
- Ser mais flexível na função
- Evita erros com parâmetros incorretos
- Nos permite trabalhar com exemplos mais legíveis de código

Quais tipos de dados podemos utilizar para valores Default?
- Qualquer tipo de dado: números, strings, floats, booleanos, listas, tuplas, dicionarios, funções, etc...
"""


# Funcções como parâmetros
def soma(num1, num2):
    return num1 + num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


def subtracao(num1, num2):
    return num1 - num2


print(mat(2, 3))
print(mat(2, 5, subtracao))

# Escopo - Para evitar problemas e confuções
"""
OBS: Se tivermos uma variável local com o mesmo nome de uma variável global, a local terá preferência.

-Atenção-
Cuidado com as variáveis globais (Se puder evitar, evite)
"""
instrutor = 'Geek'  # Varável Global


def diz_oi():
    instrutor = 'Python'  # Variável local
    return f'Oi {instrutor}'


print(diz_oi())

total = 0


def incrementa():
    global total  # Avisando que queremos utilizar a variável Global

    total = total + 1
    return total


print(incrementa())
print(incrementa())
print(incrementa())


# Podemos ter funções que são declaradas dentro de função (Forma especial de escopo de variável)
def fora():
    contador = 0

    def dentro():
        nonlocal contador  # Variável que está na função anterior
        contador = contador + 1
        return contador
    return dentro()


print(fora())
print(fora())  # Toda vez que inicializo a função o contador volta a ser zerado
print(fora())
