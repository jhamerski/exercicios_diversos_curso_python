"""
PACOTES

Módulo -> São apenas arquivos Python que pode ter diversas funções para utilizarmos.

Pacote -> Diretório contendo uma coleção de módulos.

Nas versões 2.x do Python, um pacote Python deveria conter dentro dele um pacote arquivo chamado __init__.py

Nas versões 3.x do Python, não é mais obrigatório a utilização deste arquivo, mas normalmente ainda é utilizado para
manter compatibilidade
"""
from modulo_pacote import programa1, programa2
from modulo_pacote.pacote_interno import programa3, programa4

print(programa1.pi)
print(programa1.funcao1(3, 4))
f
print(programa2.curso)
print(programa2.funcao2())

print(programa3.funcao3())
print(programa4.funcao4())

from modulo_pacote.programa1 import pi
print(pi)

from modulo_pacote.pacote_interno.programa4 import funcao4
print(funcao4())
