"""
DEFAULT DICT

https://docs.python.org/3.8/library/collections.html#module-collections

Ao criar um dicionário utilizando o Default Dict, nós informamos um valor default, podendo utilizar um lambda para isso.
Este valor será sempre utilizado sempre que não houver um valor definido. Caso tentarmos acessar uma chave que não existe
essa chave será criada e o valor será atribuido

Lambdas: São funções que podem ou não receber parâmetros de entrada e retornar valores
"""
from collections import defaultdict

dicionario = {'Aluno': 'Jonas Hamerski'}
print(dicionario)

print(dicionario['Aluno'])

# print(dicionario['Outro']) -> Gera KeyError

dicionario_dois = defaultdict(lambda: 0)

dicionario_dois['Aluno'] = 'Jonas Hamerski'
print(dicionario_dois)

print(dicionario_dois['outro'])  # Dicionário comum, iria gerar KeyError
print(dicionario_dois)


