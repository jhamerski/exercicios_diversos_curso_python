"""
FUNÇÕES COM PARÂMETROS

Funções que recebem dados para serem processados dentro da mesma
entrada ->processamento ->saída

Funções podem receber N parâmetros, ou seja, podemos receber quantos parâmetros forem necessários, são separados por
vírgula (,)

Parâmetros: São variáveis declaradas na definição de uma função.
def teste(parametro):
    # Instruções
OBS: A ordem os parâmetros, importam

Argumentos: São dados passados durante a execução de uma função
print(teste(12))
"""


# Passando parâmetros
def quadrado(numero):
    #  return numero * numero
    return numero ** 2


print(quadrado(10))
print(quadrado(7))


def cantar_parabens(aniversariante):
    print('Parabéns para você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva a/o {aniversariante}!!!')


print(cantar_parabens('Jonas'))


def soma(a, b):  # parâmetros
    return a + b


print(soma(1231, 8723))  # Argumentos


def outra(num1, b, msg):
    return (num1 + b) * msg


print(outra(2, 10, 'Jonas '))


# Nomeando parâmetros
def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'


print(nome_completo('Jonas', 'Hamerski'))

# Argumentos nomeados (KeyWord Arguments)

# Utilizando nome dos parâmetros, neste caso, podemos utilizar qualquer ordem
print(nome_completo(nome='Jonas', sobrenome='Hamerski'))
print(nome_completo(sobrenome='Hamerski', nome='Jonas'))


# Erro comum na utilização do return
def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total


lista = [1, 2, 3, 4, 5]

print(soma_impares(lista))
