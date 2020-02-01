"""
TESTE DE MEMÓRIA COM GENERATOR

Sequência de Fibonacci
1, 1, 2, 3, 5, 8, 13...


"""

# Função usando listas 475MB - TESTE 1 LISTA
def fib_lista(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums


print(fib_lista(7))

# Teste com listas
for n in fib_lista(100000):
    print(n)


# Função usando geradores
def fib_gen(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador += 1


# Teste com geradores 2.5MB
for n in fib_gen(100000):
    print(n)
