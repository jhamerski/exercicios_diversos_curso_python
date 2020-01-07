def fatorial(n):
    if n == 0:  # Fatorial de 0 é 1
        return 1
    return n * fatorial(n - 1)


print(fatorial(0))
