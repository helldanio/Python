# quantidade não-determinada (não-definida) de repetições: while

# quantidade determinada/definida de repetições: for ... in range()

# valor inicial (padrão/inclusivo): 0
# valor final (dado/exclusivo): 10
# passo/incremento (padrão): 1
for contador in range(10):
    print(contador)

# valor inicial (dado/inclusivo): 1
# valor final (dado/exclusivo): 10
# passo/incremento (padrão): 1
for contador in range(1, 10):
    print(contador)

# valor inicial (dado/inclusivo): 1
# valor final (dado/exclusivo): 10
# passo/incremento (dado): 2
for contador in range(1, 10, 2):
    print(contador)

# for regressivo (de trás pra frente)
for contador in range(20, 0, -1):
    print(contador)

