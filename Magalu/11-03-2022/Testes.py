def fatorial(n):
    fatorial = n
    for antecessor in range(n-1, 0, -1):
        fatorial *= antecessor
    return fatorial

fatorial(5)