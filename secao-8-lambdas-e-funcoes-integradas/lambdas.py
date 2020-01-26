"""
LAMBDAS

Conhecidas por expressões lambdas, ou apenas lambdas. São funções sem nome, ou seja, funções anônimas

OBS: São aplicadas para filtrar e ordenação de dados
"""


# Função Python
def funcao(x):
    return 3 * x + 1


print(funcao(4))

# Expressão lambda
lambda x: 3 * x + 1


# E como utilizar a expressão acima?
calc = lambda x: 3 * x + 1
print(calc(4))

# Podemos ter expressões lambdas de múltiplas entradas
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
# strip remove os espaços das variáveis
print(nome_completo('jonas', 'hamerski'))
print(nome_completo('   JONAS     ', '  hamerski'))

# Podemos não ter entrada ou ter N entradas
amar = lambda : 'Como não amar python?'
print(amar())
# n = lambda x1, x2, ... Xn : <expressão>
# Se passarmos mais argumentos do que parâmetros esperados, teremos TYPE ERROR

autores = ['Issac Asimov', 'Douglas Adams', 'Franck Herbert', 'Arthur C. Clarke', 'H. G. Wells']
print(autores)

# Ordenando pelo sobrenome
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)


# Função quadrática -> f(x) = a * x ** 2 + b * x * c
def geradora_funcao_quadratica(a, b, c):
    """Retorna a função: f(x) = a * x ** 2 + b * x * c"""
    return lambda x: a * x ** 2 + b * x * c


teste = geradora_funcao_quadratica(2, 3, -5)
print(teste(0))
print(teste(1))
print(teste(2))

print(geradora_funcao_quadratica(1, 2, 3)(5))
