"""
GERADORES (GENERATORS)

Generators são Iterators

OBS: O contrário não é verdadeiro, ou seja, nem todo iterador é generator

Outras informações:
    - Generators podem ser criador com funções geradoras
    - Funções geradoras utilizam a palavra reservada yield
    - Generators podem ser criados com expressões geradoras.

Diferença entre funções e Generator Functions (Funções Geradoras)
------------------------------------------------------------------------------------
| Funções                               | Generator Functions                      |
------------------------------------------------------------------------------------
| utilizam return                       | utilizam yield                           |
------------------------------------------------------------------------------------
| retorna uma vez                       | pode utilizar yield múltiplas vezes      |
------------------------------------------------------------------------------------
| quando executada, retorna um valor    | quando executado, retorna um generator   |
------------------------------------------------------------------------------------
"""


# Exemplo Generator Function (Função Geradora). OBS: Ela náo é um generator. Ela gera um generator
def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador += 1


gen = conta_ate(5)
print(type(gen))

print(next(gen))
print(next(gen))

print('------------------')

for num in gen:
    print(num)


