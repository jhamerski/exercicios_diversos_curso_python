"""
LEITURA DE ARQUIVO

Para ler o conteudo de um arquivo em Python, utilizamos a função integrada open(), que literalmente significa abrir.

open() -> A forma mais simples de utilização, nós passamos apenas um parâmetro de entrada, que nesse caso é o nome do
arquivo a ser lido. Essa função retorna um _Io.TextIOWrapper e é com ele que trabalhamos então.

https://docs.python.org/3/library/functions.html#open

Por padrão a função open() abre o arquivo para leitura. Este arquivo deve existir, ou então teremos o erro
FileNotFountError

read() -> Lê todo o conteudo do arquivo
"""

arquivo = open('texto.txt')

ret = arquivo.read()
print(ret)
print(type(ret))


print(arquivo)
print(type(arquivo))

# Para ler um arquivo, aspós sua abertura devemos utilizar a função read()

arquivo = open('texto.txt')
print(arquivo.read())  # Não acontece nada, porque o cursor está no final do arquivo
