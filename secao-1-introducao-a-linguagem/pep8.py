"""
PEP8 - Python Enhancement Proposal

Propostas de melhorias para a linguagem Python

import this - The Zen Of Python

Regras:
[1] - Utilize Camel Case para nome das classes
class Calculadora:
    pass

class CalculadoraCientifica:
    pass

[2] - Utilize nomes em mínusculo, separados por underline para funções e variáveis
def soma():
    pass

def soma_dois():
    pass

numero = 4
numero_impar = 5

[3] - Utilize 4 (quatro) espaços para identação (NÃO use tab)
if 'a' in 'banana':
    print('Tem')

[4] - Linhas em branco
*Separar funções e definições de classes com 2 (duas) linhas em branco
*Métodos dentro de uma classe, deve ser separado com 1 (uma) linha em branco

[5] - Imports deve ser feito em linhas separadas e deve ficar no topo do arquivo
(logo depois de quaisquer comentários ou DocStrings)

    Errado                     Certo
import sys, os              import sys
                            import os

*Varios imports
from types import(
    StringType,
    ListType,
    SetType
)

[6] - Espaços em expressçoes e instruções
            *Errado                                     *Certo
algo ( 1 )                                     algo(1)
funcao ( algo [ 1], { outro: 2} )              funcao(algo[1], {outro:2})
dict ['chave'] = list ['indice1']              dict['chave'] = list['indice1']
x              = 1                             x = 1
variavel_longa = 2                             variavel_longa = 2

[7] - Termine sempre com 1 (uma) linha em branco
"""

