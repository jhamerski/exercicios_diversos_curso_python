"""
(TUPLAS) - tuple

São parecidas com listas, temos duas principais diferenças entre elas, que são:
- Tuplas são representadas por (parênteses) mas a DEFINIÇÃO dela é feita pela vírgula(,)
    * (4) - Não é tupla.
    *  4, - É tupla.
    * (4,) - É tupla
- São IMUTÁVEIS, ao criar uma tupla ela não muda e ao realizarmos uma operação é gerada uma nova tupla.
"""
tupla = (1, 2, 3, 4, 5)
print(tupla)
print(type(tupla))

tupla_one = 1, 2, 3, 4, 5
print(tupla_one)
print(type(tupla_one))

# CUIDADO: Não é considerado uma tupla
tupla_two = (1)
print(tupla_two)
print(type(tupla_two))

# Isso é uma tupla
tupla_three = (1,)
print(tupla_three)
print(type(tupla_three))

# Podemos gerar uma tupla dinâmicamente com range(inicio:fim:passo)
tupla_four = tuple(range(11))
print(tupla_four)

# Desempacotamento de tupla. OBS: O número de elementos precisa ser o MESMO do número de variáveis, senão VALUE ERROR
tupla_five = ('Jonas', 'Hamerski', 1987)
nome, sobrenome, ano = tupla_five
print(f'{nome} {sobrenome} nasceu em {ano}')

# Métodos para adição e remoção NÃO EXISTEM nas tuplas, pois elas são imutáveis.
# Soma*, valor Máximo*, valor Mínimo* e tamanho (*Todos valores inteiros ou reais)
tupla_six = (1, 2, 3, 4, 5, 6)
print(sum(tupla_six))
print(max(tupla_six))
print(min(tupla_six))
print(len(tupla_six))

# Concatenação de tuplas
tupla_seven = (1, 2, 3)
tupla_eigth = (4, 5, 6)
print(tupla_seven)
print(tupla_eigth)
print(tupla_seven + tupla_eigth)
print(tupla_seven)
print(tupla_eigth)
tupla_seven = tupla_seven + tupla_eigth  # sobrescrevendo o valor da tupla_seven
print(tupla_seven)

# Verificar se tem um X na tupla
print(3 in tupla_seven)

# Iterando em tupla
for elemento in tupla_seven:
    print(elemento)

for indice, valor in enumerate(tupla):
    print(indice, valor)

# Cotando elementos
tupla_nine = ('a', 'b', 'c', 'd', 'a', 'b')
print(tupla_nine.count('a'))
print(tupla_nine.count('c'))
print(tupla_nine.count('b'))

escola = tuple('Geek University')
print(escola)
print(escola.count('e'))

"""
DICAS:
- Devemos utilizar tuplas, sempre que não precisarmos modificar os dados contidos em uma coleção
Exemplo:
    Janeiro, Fevereiro, ..., Dezembro
"""
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
         'Novembro', 'Dezembro')
print(meses[3])

# Iterar com While
i = 0
while i < len(meses):
    print(meses[i])
    i = i + 1

# Verificando em qual índice está um elemento X
print(meses.index('Agosto'))  # Se o elemento não existir, vai gerar VALUE ERRO

# slicing() -> (início/fim/passo)
print(meses[0:])

# Por quê utilizar tuplas?
# - São mais rápidas do que listas.
# - Deixam o código mais seguros.

# Na tupla não temos Shallow Copy
