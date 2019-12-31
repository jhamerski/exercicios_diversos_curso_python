"""
CONJUNTOS

 - Em qualquer linguagem de programação, estamos fazendo referência à Teoria dos Conjuntos Matemáticos

Aqui em Python, são chamados de SETS

 - Da mesma forma que na matemática:
    - Sets (conjuntos) não possuem valores repetidos.
    - Sets (conjuntos) não possuem valores ordenados.
    - Elementos não são acessados via índice, ou seja, conjuntos não são indexados.

Conjuntos SÂO BONS para quando precisarmos armazenar elementos e não nos importamos com a ordenação deles. Quando não
precisamos se preocupar com chaves, valores ou itens duplicados.

Os conjuntos (sets) são representados por {chaves}

Diferença entre Conjuntos (sets) e Mapas (dict) em Python:
    - Um dicionário tem chave/valor.
    - Um conjunto tem apenas valor.

"""
# Definindo um conjunto
s = set({1, 2, 3,4, 5, 6, 2, 3, 4, 3, 2})  # Aqui temos valores repetidos
print(s)  # Se adicionarmos um valor já existente, o mesmo será ignorado e não vai gerar ERRO
print(type(s))

s = {1, 2, 3, 4, 5, 6, 2, 3, 4, 3, 2}
print(s)
print(type(s))

# Verificando se determinado elemento está contigo no conjunto
if 3 in s:
    print('Tem o 3')

# Podemos misturar os tipos de dados em conjuntos
s = {1, 'b', 1.34, True, 44}
print(s)
print(type(s))

# Iterando
for valor in s:
    print(valor)

"""
USO DOS SETS: 
- Imagine que fizemos um formulário de cadastros em uma feira ou museu, os visitantes informam manualmentea cidade de 
onde vieram, nós adicionamos cada cidade em uma lista de elemtos, já que as listas são mutáveis e podemos ter repetição
de valores.
"""
cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiabá', 'São Paulo', 'Cuiabá', 'Florianópolis', 'São Paulo']
print(len(cidades))

# Agora precisamos saber quantas cidades distintas/únicas temos? O que você faria?
print(len(set(cidades)))

# Adicionando elementos
s = {1, 2, 3, 4}
s.add(5)
s.add(5)  # Não gera ERRO, apenas não adiciona o elemento
print(s)

# Remover elementos
print(s)
s.remove(4)  # Se o valor não existir, gera KEY ERROR
print(s)

s.discard(1)  # Se o valor não existir, NÃO GERA ERRO
print(s)

# Copiando um conjunto para outro
novo = s.copy()  # Deep Copy
print(novo)
novo.add(4)
print(s)
print(novo)

new = s  # Shallow Copy
new.add(1)
print(new)
print(s)

# Removendo todos os itens
s.clear()
print(s)

"""
Métodos Matemáticos dos Conjuntos
 - Imagine que temos dois conjuntos: um com estudantes do curso Pyhon e um contendo estudantes Java
"""
estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# OBS: Alguns alunos estão nos dois cursos
# Gerar conjunto com estudantes únicos
# UNION
unicos_um = estudantes_python.union(estudantes_java)
print(unicos_um)

# Utilizando o pipe |
unicos_dois = estudantes_python | estudantes_java
print(unicos_dois)

# Gerar conjunto que estão em ambos cursos
ambos_um = estudantes_python.intersection(estudantes_java)
print(ambos_um)

# Utilizando o &
ambos_dois = estudantes_python & estudantes_java
print(ambos_dois)

# Gerar conjunto de estudantes que não estão no outro
so_python = estudantes_python.difference(estudantes_java)
print(so_python)
so_java = estudantes_java.difference(estudantes_python)
print(so_java)

# Soma*, valor máximo*, valor mínimo*, tamanho. OBS: Todos devem ser int ou float
s = {1, 2, 3, 4, 5, 6}
print(sum(s))
print(max(s))
print(min(s))
print(len(s))

