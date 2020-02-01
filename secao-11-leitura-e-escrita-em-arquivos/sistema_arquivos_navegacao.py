"""
SISTEMAS DE ARQUIVOS E NAVAGAÇÃO

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos fazer o uso do módulo OS
os -> Operating System (Sistema Operacional)

# Podemos checar se um diretório é absoluto ou relativo
print(os.path.isabs('C:\\Users\\55489\\PycharmProjects'))

# Verificando no nome do sistema operacional
print(os.name)  # posix (LINUX ou MAC) nt (WINDOWS)

# Veja que o os.path.join() recebe dois parâmetros, sendo o primeiro o diretório atual e o segundo o diretório novo
print(os.getcwd())

res = os.path.join(os.getcwd(), 'nova_pasta')
os.chdir(res)

print(os.getcwd())

"""
import os

# getcwd() -> pega o current work directory (diretório de trabalho corrente)
print(os.getcwd())

# Para mudar o diretório, podemos utilizar o chdir
os.chdir('..')

print(os.getcwd())

# Podemos listar os arquivos e diretórios com o listdir()
print(len(os.listdir()))

print(len(os.listdir('C://')))

# Podemos listar os arquivos com mais detalhes com o scandir()
print(list(os.scandir()))

arquivos = list(os.scandir())

print(arquivos[0].is_dir())
print(arquivos[0].is_file())
