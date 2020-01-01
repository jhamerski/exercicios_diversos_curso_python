"""
DEQUE

Podemos dizer que o deque é uma lista de alta performance.
"""
from collections import deque

# Criando
deq = deque('Jonas')
print(deq)

# Adicionando elementos
deq.append('!')  # Adiciona no final
print(deq)

deq.appendleft('-')  # Adiciona no início
print(deq)

# Remover
deq.pop()  # Remove e retorna o último elemento
print(deq)

deq.popleft()  # Remove e retorna o primeiro elemento
print(deq)
