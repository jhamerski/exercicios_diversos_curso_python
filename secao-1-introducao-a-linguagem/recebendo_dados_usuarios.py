"""
RECEBENDO DADOS

dir(__builtins___) -> São recursos integrados da linguagem

Todo dado recebido via input é String
Strings em Puthon são tudo que estiver entre:
- Aspas simples, aspas duplas, aspas simples triplas e aspas duplas triplas
"""
# Entrada de dados
nome = input('Qual seu nome...')

print(f'Seja bem vindo(a) {nome}!')

idade = int(input('Qual a sua idade...'))

# Exemplo de print antigo 2.x
# print('O(A) %s tem %s anos!' % (nome, idade))

# Exemplo de print moderno - Criado a partir da versão 3.x
# print('O(A) {0} tem {1} anos!'.format(nome, idade))

# Forma atual - Criado a partir de 3.6 ou 3.7
print(f'O(A) {nome} tem {idade} anos!')

# cast é a conversão de um tipo de dado para outro
print(f'O(A) {nome} nasceu em {2019 - idade}!')
