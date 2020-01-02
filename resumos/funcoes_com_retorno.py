"""
FUNÇÕES COM RETORNO

Funções que retornam valores, devem retornar estes valores com a palavra reservada "return"
OBS:
- Não precisamos necessariamente criar uma variável para receber o retorno de uma função. Podemos passar a execução da
função para outras funções

OBS:
- Quando uma função não retorna nenhum valor, o retorno é None.

Sobre RETURN:
- Ela finaliza a função, ou seja, ela sai da execução da função.
- Podemos ter em uma função, diferentes returns.
- Podemos retornar qualquer tipo de dado e até múltiplos valores.
"""
from random import random
numeros = [1, 2, 3]

ret_pop = numeros.pop()

print(f'Retorno de pop(): {ret_pop}')

ret_pr = print(numeros)

print(f'Retorno de print(): {ret_pr}')


# Função sem retorno
def quadrado_de_sete():
    print(7 * 7)  # Estamos imprimindo, não retornando.


ret_qds = quadrado_de_sete()

print(f'Retorno ret: {ret_qds}')


# Vamos refatorar a função acima, para que ela tenha retorno
def quadrado_de_sete_refatorado():
    return 7 * 7


# Criamos uma variável para receber o retorno da função
ret_qdsr = quadrado_de_sete_refatorado()
print(f'O retorno de quadrado_de_sete_refatorado(): {ret_qdsr}')

# Abaixo temos o retorno diretamente dentro do print
print(f'Retorno: {quadrado_de_sete_refatorado()}')


def diz_oi():
    return 'Oi!'


print(diz_oi())


def diz_outro_oi():
    print('Estou sendo executado antes do retorno!')
    return 'Oi!'
    print('Estou sendo executado depois do retorno!')  # Nunca será executada essa linha


print(diz_outro_oi())


# Vários tipos de returns
def nova_funcao():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'


print(nova_funcao())


def outra_funcao():
    return 2, 3, 4, 5


print(outra_funcao())
print(type(outra_funcao()))

num1, num2, num3, num4 = outra_funcao()
print(num1, num2, num3, num4)


# Crian função jogar moeda
def joga_moeda():
    if random() > 0.5:  # Gera um número pseudo-randômico entre (0 e 1)
        return 'Cara'
    else:
        return 'Coroa'


print(joga_moeda())


# Codificação desnecessária
def eh_impar():
    numero = 5
    if numero % 2 != 0:
        return True
    return False  # Nessa linha é desnecessário a utilização do else


print(eh_impar())
