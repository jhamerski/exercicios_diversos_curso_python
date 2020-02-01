"""
BLOCO WITH

Passos para se trabalhar com arquivos
1) Abrimos
2) Manipulamos
3) Fechamos

O bloco with é utilizado para criar um contexto de trabalho, onde os recursos utilizados são fechados após o bloco with
"""
# É a forma Pythônica para se trabalhar com arquivos
with open('texto.txt') as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed)

print(arquivo.closed)
