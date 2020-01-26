"""
FILTER

Serve para filtrar dados de uma determinada coleção. Assim como a função map, a filter() recebe dois parâmetros. Sendo
1° função e 2° iterável

"""
# Biblioteca para trabalhar com dados estatísticos
import statistics
valores = 1, 2, 3, 4, 5, 6
media = (sum(valores) / len(valores))

print(media)

dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)
print(f'Média dos dados é: {media}')

res = filter(lambda x: x > media, dados)
print(list(res))

# Assim como em map(), após serem utilizados os dados do filter(), eles são excluídos da memória.
print(f'Aqui perdemos os dados do filter: {list(res)}')

# Removendo dados faltantes
paises = ['', 'Argentinha', '', 'Brasil', 'Chile', '', 'Equador', '', '', 'Venezuela']
print(paises)
res = filter(None, paises)  # Tipo sem tipo, ou tipo vazio
print(list(res))

outro_res = filter(lambda pais: len(pais) > 0, paises)
print(list(outro_res))

terceira_res = filter(lambda pais: pais != '', paises)
print(list(terceira_res))

"""
A diferença entre map() e filter() é:
map() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto mapeando a função para cada elemento
iterável.
filter() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto FILTRANDO APENAS OS ELEMENTOS de acordo
com a função

Resumindo, a função filter(), sempre vai retornar True or False, enquanto map() retornam todos os valores.
"""
usuarios = [
    {'username': 'jonas', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
    {'username': 'carlos', 'tweets': ['Eu amo gatos']},
    {'username': 'julia', 'tweets': []},
    {'username': 'francielle', 'tweets': []},
    {'username': 'arthur', 'tweets': ['Eu gosto de carne', 'Vou sair hoje']},
    {'username': 'paulo', 'tweets': []},
]
print(usuarios)

# Filtrar os usuários que estão inativos no Twitter
inativos = list(filter(lambda u: len(u['tweets']) == 0, usuarios))
print(inativos)

# Refatorando
inativos_dois = list(filter(lambda u: not u['tweets'], usuarios))  # lista vazia [] é False
print(inativos_dois)

# Combinar filter() e map()
nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo 'Sua instrutora é:' + nome, desde que cada nome tenha menos de 5 caracteres
lista = list(map(lambda nome: f'Sua instrutora é: {nome}', filter(lambda nome: len(nome) < 5, nomes)))
print(lista)

