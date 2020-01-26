"""
DICIONÁRIOS

Em algumas linguagens DICIONÁRIOS são conhecidos por MAPAS.
São coleções do tipo chave/valor.

São representados por {chaves}
SOBRE:
    - Chave e valor são separados por : (dois pontos)
    - Tanto chave quanto valor, podem ser de qualquer tipo de dados
    - Podemos misturar tipos de dados
    - Sempre é considerado como False
"""
print({})

# Criação
paises = {'br': 'Brasil', 'eua': 'Estados Unidos das Américas', 'py': 'Paraguai'}
print(paises)
print(type(paises))

paises_um = dict(br='Brasil', eua='Estados Unidos das Américas', py='Paraguai')
print(paises_um)
print(type(paises_um))

# Acessando elementos
# Via chave, se a chave não existir, gera o KEYERROR
print(paises['br'])
print(paises['py'])

# Via get (recomendado), quando a chave não existir, gera tipo de dado NONE e não retorna o KEYERROR
print(paises.get('eua'))
print(paises.get('br'))
print(paises.get('ru'))

russia = paises.get('ru')
if russia:
    print('Encontrei o país.')
else:
    print('Não encontrei o país.')

pais = paises.get('ru', 'Não encontrado')  # definimos um valor padrão para objeto com chave inexistente
print(f'Encontrei o pais {pais}')

pais = paises.get('py', 'Não encontrado')
print(f'Encontrei o pais {pais}')

# Verificando se determinada chave existe no dicionário
print('br' in paises)
print('ru' in paises)
print('Paraguai' in paises)

# São aceitos todos tipos de dados: Inclusive tuplas, listas
localidades = {(35.6895, 39.6917): 'Escritório em Tóquio', (40.456, 41.987): 'Escritório em Nova York'}
print(localidades)
print(type(localidades))

# Adicionar elementos
receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)
print(type(receita))

receita['abr'] = 450
print(receita)

novo_dado = {'mai': 500}
receita.update(novo_dado)  # receita.update({'mai': 500})
print(receita)

# Atualizando
receita['mai'] = 550
print(receita)

receita.update({'mai': 600})
print(receita)
# A forma de adicinar ou atualizar dados em um dicionário é a mesma. Outro fator é que não podemos ter chaves repetidas

# Remover
receita.pop('mar')  # Aqui precisamos SEMPRE informar a chave, caso não encontrar, retorna KEYERROR
ret = receita.pop('jan')  # Remove a chave desejada e retorna o valor que era atribuído a ela
print(ret)
print(receita)

del receita['mai'] # Se a chave não existir, retorna KEYERROR, nesse caso o valor removido não é retornado
print(receita)

"""
Imagine que você tem um comércio eletroônico, e-commerce. Onde temos um carrinho de comprar na qual adicionamos prod.
Carrinho de compras:
    Produto 01
    - Nome
    - Quantidade
    - Preço
    
    Produto 02
    - Nome
    - Quantidade
    - Preço
"""
# Poderiamos utilizar uma lista? SIM
# Teríamos que saber qual é o índice de cada informação do produto
carrinho = []
produto_um = ('Play Station 4', 1, 2300.00)
produto_dois = ('God of War 4', 1, 150.00)

carrinho.append(produto_um)
carrinho.append(produto_dois)
print(carrinho)

# Poderiamos utilizar uma tupla? SIM
# Teríamos que saber qual é o índice de cada informação do produto
produto_tres = ('Play Station 4', 1, 2300.00)
produto_quatro = ('God of War 4', 1, 150.00)
carrinho_um = (produto_tres, produto_quatro)
print(carrinho_um)

# Poderiamos utilizar um dicionário? SIM, desta forma adicionamos ou removemos produto no carrinho, contendo todas
# informações
carrinho_dois = []
produto_cinco = {'nome': 'Play Station 4', 'quantidade': 1, 'preco': 2300.00}
produto_seis = {'nome': 'God Of War 4', 'quantidade': 1, 'preco': 150.00}
carrinho_dois.append(produto_cinco)
carrinho_dois.append(produto_seis)
print(carrinho_dois)

# Métodos dir({})
d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

# limpar (zerar dados)
# d.clear()
print(d)

novo = d.copy()  # Deep Copy
print(novo)

novo['d'] = 4
print(d)
print(novo)

new = d  # Shallow Copy
new['e'] = 6
print(d)
print(new)

# Forma não usual de criação
# fromkeys() recebe dois parâmetros: um iterável, outro valor.
outro = {}.fromkeys('a', 10)
print(outro)
print(type(outro))

veja = {}.fromkeys('teste', 'valor')
print(veja)

usuario = {}.fromkeys(['nome', 'e-mail', 'profile', 'pontos'], 'desconhecido')
print(usuario)
print(type(usuario))

veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)

