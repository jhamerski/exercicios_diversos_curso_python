"""
COUNTER

COLLECTIONS -> High Performance Container DataTypes

 - Recebe um iterável como parâmetro e cria um objeto do tipo Collection Counter, que é parecido com um dicionário,
contendo como chave o elemento da lista passado como parâmetro e como valor a quantidade de ocorrências desse elemento.
"""
# Utilizando o Counter
from collections import Counter

lista = [1, 1, 2, 3, 3, 3, 2, 2, 1, 2, 3, 3, 4, 5, 4, 4, 4, 5, 5, 12, 53, 87, 87]

res = Counter(lista)

print(res)  # para cada elemento da lista o Counter criou uma chave e colocou como valor a quantidade de repetição
print(type(res))

print(Counter('Jonas Hamerski'))

texto = """
O que é Python?
    Antes de entrarmos no aspecto teórico do que é Python, gostaríamos de citar duas características que a tornam uma 
linguagem de programação particularmente atrativa. Python é uma linguagem simples e fácil de aprender. Quem já tentou 
aprender C ou C++ sabe que as particularidades da linguagem em si tornam o aprendizado de programação muito mais 
desafiador. Com Python, pelo fato de a linguagem ser simples, o aprendizado dos conceitos de programação e algoritmos 
assumem o papel principal que lhes é devido na trajetória de aprendizado de alguém.
    Além disso, Python possui um número gigante de bibliotecas disponíveis. Assim, para a maioria das tarefas, você 
encontrará uma biblioteca que facilitará muito sua vida. Com isso, você não precisa ficar reinventando a roda toda vez 
que quiser escrever um programa para resolver um problema específico.
    Agora podemos partir para a explicação mais teórica sobre que é Python.
Em poucas palavras, Python é uma linguagem de programação:
- propósito geral,
- interpretada,
- dinamicamente tipada.
"""

palavras = texto.split()

print(palavras)

res = Counter(palavras)
print(res)

# Encontrando as 5 palavras com maior ocorrências no texto
print(res.most_common(5))
