"""
STRING IO

ATENÇÃO: Para ler e escrever dados em arquivos do sistema operacional o softeware precisa ter permissão:
    - Permissão de leitura: Para ler o arquivo.
    - Permissão de escrita: Para escrever o arquivo.

StringIO -> Utilizados para ler e criar arquivos em memória.
"""
# Primeiro fazemos o import
from io import StringIO
mensagem = 'Está é apenas uma string normal'

# Podemos criar um arquivo em memória já com uma string inserida ou mesmo vazio, para inserirmos texto depois
arquivo = StringIO(mensagem)  # arquivo = open('arquivo.txt', 'w')

print(arquivo.read())

# Escrevendo mais texto
arquivo.write(', outro texto.')

# Movimentando o cursor
arquivo.seek(0)
print(arquivo.read())
