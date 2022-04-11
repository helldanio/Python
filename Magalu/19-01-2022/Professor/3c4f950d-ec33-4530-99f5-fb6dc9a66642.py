# estruturas de dados

lista = [3.14, 2.7, 10, 'olá', True, 'mundo']
#indices: 0,    1,   2,   3,    4,     5

print(2.7 in lista)
print('abacate' in lista)


print(lista[4])


for indice in range(6):
    print(lista[indice])
    lista[indice] = 10

print(lista)

for elemento in lista:
    print(elemento)
    elemento = 10
