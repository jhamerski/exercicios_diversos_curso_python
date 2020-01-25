"""
ESTRUTURAS DE REPETIÇÃO

loop e for são estruturas de repetição

C or JAVA
for(int i = 0; i < limitador; i++){
    //execução do loop
}

PYTHON
for item in interavel:
    //execução do loop

Utilizamos loops para iterar sobre sequência ou sobre valores iteráveis
Exemplos:
- String
    nome = 'Jonas Hamerski'
- Listas
    lista = [1, 3, 5, 7, 9]
- Range
    numeros = range (1, 10)
"""
nome = 'Jonas Hamerski'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # Temos que transformar em uma lista

# Exemplo (String)
for letra in nome:
    print(letra, end='')

# Exemplo (Lista)
for numero in lista:
    print(numero, end='')

# Exemplo (Range) - (valor_inicial, valor_final - 1) OBS: Pois o último não é inclusive
for numero in range(1, 10):
    print(numero)

# Enumerate ((0, 'J'), (1, 'o'), (2, 'n'), (3, 'a'), (4, 's')...)
for indice, valor in enumerate(nome):
    print(nome[indice])

for indice, letra in enumerate(nome):
    print(letra)

for _, letra in enumerate(nome):
    print(letra)

for letra in enumerate(nome):
    print(letra)

qtd = int(input('Quantas vezes esse loop deve rodar: '))
for n in range(1, qtd+1):
    print(f'Imprimindo {n}')

soma = 0
for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd}: '))
    soma = soma + num
print(soma)

for num in range(1, 10):
    print('\U0001F60D' * num)
