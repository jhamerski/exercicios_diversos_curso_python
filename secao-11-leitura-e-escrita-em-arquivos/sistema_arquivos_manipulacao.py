"""
SISTEMA DE ARQUIVO DE MANIPULAÇÃO

import os
# Descobrindo se um arquivo ou diretório existe
print(os.path.exists('arquivo.txt'))  # False
print(os.path.exists('novo.txt'))  # True

# Paths Absoluto
print(os.path.exists('C:\\Users'))  # True

# Criando um arquivo
open('arquivo-teste.txt', 'a').close()
open('arquivo-teste-1.txt', 'w').close()
with open('arquivo-teste-2.txt', 'a') as arq:
    pass  # Não farei nada

# A melhor forma para criar um arquivo seria:
# os.mknod('arquivo-teste-3.txt')  # Se o arquivo ja existir, teremos o FileExistsError

# Criando diretórios
os.mkdir('templates')  # Se o arquivo já existir, teremos o FileExistsError
# Se não tiver permissão de criação em um diretório, teremos o PermissionError

# Criando multi diretórios (árvores)
os.makedirs('aaaa\\bbb\\ccc')

# Se os diretórios já existirem, eles são ignorados e não gera erro
os.makedirs('aaaa\\bbb\\ccc', exist_ok=True)

# Renomeando diretórios, se o diretório não existir, teremos o FileNotFoundError
os.rename('renomeadossssss', 'renomeado')

# Deletar -> OBS: Ao deletarmos um arquivo ou diretório, ele não vão para a lixeira, simplismente somem
# Removendo ARQUIVOS
os.remove('deletado.txt')  # No windows se o arquivo tiver aberto, terá um error
# Caso o arquivo não exista teremos o FileNotFoundError

import os
# Remover DIRETÓRIOS vazios, OBS: Se o diretório tiver qualquer conteúdo gera o OSError e se não existir FileNotFound
os.removedirs('renomeado')

# Removendo diversos arquivos de um diretório
for arquivo in os.scandir('arquivos'):
    if arquivo.is_file():
        os.remove(arquivo.path)

# Importando a biblioteca send2trash (Envia arquivos e diretórios para a lixeira)
from send2trash import send2trash

send2trash('resultado.txt')

"""
# Trabalhando com arquivos e diretórios temporários
import os
import tempfile
with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretório temporário em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('Jonas Hamerski\n')
    input()

# OBS: Estamos criando um arquivo temporário, abrindo ele, e dentro dele criando um arquivo para escrevermos um texto
# No final, usamos um input() só para mantermos os arquivos temporários 'vivos' dentro dos blocos with

# Criando um arquivo temporário
with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Jonas Hamerski')  # b é BINARY, em arquivos temporários só conseguimos escrever em bits
    tmp.seek(0)
    print(tmp.read())

# Outra forma de criar
arquivo = tempfile.TemporaryFile()
arquivo.write(b'Jonas Hamerski')
arquivo.seek(0)
print(arquivo.read())
arquivo.close()
