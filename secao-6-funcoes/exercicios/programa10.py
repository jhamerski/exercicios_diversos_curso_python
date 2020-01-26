"""
Escreva uma função que compare e retorne verdadeiro, caso uma string seja anagrama da outra, e falso, caso contrário
"""


def anagrama(texto):
    texto = list(texto)

    for i in range(len(texto)):
        if texto[i] == texto[-1]:
            return True
        return False


print(anagrama('subinoonibus'))
print(anagrama('Jonas'))
