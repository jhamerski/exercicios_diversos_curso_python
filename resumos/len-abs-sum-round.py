"""
LEN, ABS, SUM, ROUND

len() -> Retorna o tamanho (ou seja, o número de itens) de um iterável.

abs -> Retorna o valor absoluto de um número inteiro ou real. De forma básica seria o seu valor real sem o sinal

sum() -> Recebe como parâmetro um iterável, podendo receber um valor inicial e retorna a soma dos elementos, incluindo
o valor inicial. OBS: O valor inicial default é zero

round() -> Retorna um número arredondado para N digito de precisão após a casa decimal. OBS: Se a precisão não for
informada, retorna o inteiro mais próxima da entrada
"""
# len()
print(len('Jonas Hamerski'))

print(len([1, 2, 3, 4, 5, 6]))

print(len((1, 2, 3, 4, 5, 6)))

print(len({1, 2, 3, 4, 5, 6}))

print(len(range(0, 19)))

# Por debaixo dos panos, quanto utilizamos a função len() o Python faz o seguinte:
print('Jonas Hamerski'.__len__())  # Dunder len

# abs()
print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))

# sum()
print(sum([1, 2, 3, 4, 5]))

print(sum([1, 2, 3, 4, 5], 5))  # Valor inicial: 5

print(sum([3.14, 5.67]))

print(sum((1, 2, 3, 4, 5, 6)))

print(sum({1, 2, 3, 4}))

print(sum({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}.values()))

# round()
print(round(10.2))

print(round(10.5))

print(round(10.6))

print(round(1.212121212, 2))

print(round(1.2199999, 2))
