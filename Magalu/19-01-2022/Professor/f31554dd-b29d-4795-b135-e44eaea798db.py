'''
s = 1/1! + 1/2! + 1/3! + ... + 1/1000!
'''
soma = 0
fatorial = 1
contador = 1

while contador <= 1000:
    fatorial = fatorial * contador
    termo = 1/fatorial
    soma = soma + termo
    contador = contador + 1

print(soma)