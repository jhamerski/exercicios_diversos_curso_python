"""
SEEKS E CURSORES

seek() -> Utilizado para movimentar o cursor pelo arquivo

OBS: Quando abrimos um arquivo com a função open(), é criada uma conexão entre o arquivo no disco do sistema operacional
e o programa, essa conexão é chamada de streaming. Ao finalizar os trabalhamos com o arquivo, devemos fechar essa conexao
para isso utilizamos a função close()

PASSOS PARA SE TRABALHAR COM UM ARQUIVO:
- 1)Abrir o arquivo
- 2)Trabalhar com o arquivo
- 3)Fechar o arquivo

OBS:
Se tentarmos manipular o arquivo após seu fechamento, teremos ValueError
"""
# 1) Abrir arquivo
arquivo = open('texto.txt')

# 2) Trabalhando com o arquivo
print(arquivo.read())

# Momentando o cursor pelo arquivo com seek() -> Procurar
arquivo.seek(12)  # Movimentamos o cursor para a posição 12
print(arquivo.read())

# 3) Fechando o arquivo
arquivo.close()

print(30 * '-=')
arquivo = open('texto.txt')

ret = arquivo.readline()
print(type(ret))
# readlines() ->Lê o arquivo linha a linha (lê linha)
print(arquivo.readline())
print(arquivo.readline())
print(arquivo.readline())

arquivo.close()

print(30 * '-=')
arquivo = open('texto.txt')

linhas = arquivo.readlines()

print(linhas)
print(len(linhas))

# Verificando se o arquivo está aberto ou fechado
print(arquivo.closed)  # False

arquivo.close()

print(arquivo.closed)  # True

print(30 * '-=')
arquivo = open('texto.txt')

# Limitando a leitura dos arquivos
print(arquivo.read(11))

arquivo.close

