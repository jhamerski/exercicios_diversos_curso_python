import time


def hanoi(n, origem, destino, aux):
    if n == 1:  # Se tiver apenas um disco
        print(f'Mova {origem} para {destino}')
    else:
        hanoi(n - 1, origem, aux, destino)  # Movendo n-1 origem para destino
        hanoi(1, origem, destino, aux)  # Movendo um único disco para o destino
        hanoi(n - 1, aux, destino, origem)  # Movendo os n-1 aux para destino


ini = time.time()
hanoi(20, 'A', 'B', 'C')
fim = time.time()

print(f'O tempo de execução durou {fim - ini}')
