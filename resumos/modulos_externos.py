"""
MÓDULOS EXTERNOS

Utilizamos o gerenciador de pacotes Python chamado Pip -> Python Installer Package

Você pode conhecer todos os pacotes oficiais e externos em https://pypi.org

Instalando um módulo: pip install 'nome_do_modulo'

# pip install colorama
from colorama import (
    init,
    Fore,
    Back,
    Style
)
init()

print(Fore.RED + 'Jonas Hamerski')
print(Fore.BLUE + 'Jonas Hamerski')
print(Fore.GREEN + 'Jonas Hamerski')
"""
import pydf

pdf = pydf.generate_pdf('<h1>Jonas Hamerski</h1>')

with open('test doc.pdf', 'wb') as f:
    f.write(pdf)
