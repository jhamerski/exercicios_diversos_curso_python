"""
DEBUGANDO COM PDB (PYTHON DEBUGGER)

OBS: A partir do PYTHON 3.7, não precisamos mais importar a biblioteca PDB, pois o comando de debug, foi incorporado
como uma função built-in (integrada) chamada breakpoint()

Cuidado com os nome das variáveis e os comandos pdb() 'l, n, p, c'
"""


# A utilização do print() para debugar código, é uma prática ruim.
def dividir_um(a, b):
    print(f'a = {a}, b = {b}')
    try:
        return float(a) / float(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu o erro: {err}'


print(dividir_um(4, 7))


# Formas melhores e mais profissionais de fazer o Debugger
# Exemplo com PyCharm
def dividir_um(a, b):
    try:
        return float(a) / float(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu o erro: {err}'


print(dividir_um(4, 0))

# Exemplo com PDB, precisamos importar a biblioteca PDB e utilizar a função set_trace(), temos que utilizar comandos
"""
 l (listar onde estamos no código)
# n (próxima linha)
# p (imprime variável)
# c (continua a execução - finaliza o debugging)
"""
import pdb
nome = 'Jonas'
sobrenome = 'Hamerski'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python'
final = nome_completo + ' faz o curso ' + curso
print(final)


# Outro exemplo com PDB
"""
 Por quê utilizamos esse formato? O debug é utilizado durante o desenvolvimento. Costumammos realizar todos os imports 
 de bibliotecas no início do arquivo. Por isso ao invés de colocarmos o import no começo do arquivo, nós colocamos 
 somente onde vamos debuggar e ao finalizar já fizemos a remoção.
"""
nome = 'Jonas'
sobrenome = 'Hamerski'
import pdb; pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python'
final = nome_completo + ' faz o curso ' + curso
print(final)

# Novo PDB a partir da versão 3.7 (breakpoint())
nome = 'Jonas'
sobrenome = 'Hamerski'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python'
final = nome_completo + ' faz o curso ' + curso
print(final)


def soma(l, n, p, c):
    breakpoint()
    return l + n + p + c


# Cuidado com os nome das variáveis e os comandos pdb() 'l, n, p, c'. Basta selecionar a opção p 'imprimir' e escolher
# a opção desejada, ou seja, p + nome da variável
print(soma(1, 2, 3, 4))
