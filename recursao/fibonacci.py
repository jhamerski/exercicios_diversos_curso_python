def fib(n):
    if n <= 1:  # Calculando os dois primeiros termos
        return n
    return fib(n - 1) + fib(n - 2)  # Cálculo do n-ésimo termo


print(fib())
