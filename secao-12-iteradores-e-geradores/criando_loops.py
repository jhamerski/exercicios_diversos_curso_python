"""
CRIANDO LOOPS (PRÓPRIA VERSÃO)

for num in [1, 2, 3, 4, 5]:
    print(num)

for letra in 'Jonas':
    print(letra)

iter([1, 2, 3, 4, 5])

iter('Jonas')
"""


def meu_for(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


meu_for('Jonas')
numeros = [1, 2, 3, 4, 5]
meu_for(numeros)
