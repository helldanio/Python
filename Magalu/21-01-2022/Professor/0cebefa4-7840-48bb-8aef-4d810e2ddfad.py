'''
Faça um programa que, dadas duas listas de mesmo tamanho, crie uma nova lista com cada 
elemento igual a soma dos elementos da lista 1 com os da lista 2, na mesma posição.

Exemplo:

Dadas lista1 = [1, 4, 5] e lista2 = [2, 2, 3], então lista3 = [1+2, 4+2, 5+3] = [3, 6, 8]
'''

'''
lista1 = [1, 4, 5]
lista2 = [2, 2, 3]

lista3 = []

for indice in range(len(lista1)):
    soma = lista1[indice] + lista2[indice]
    lista3.append(soma)

print(lista3)
'''

'''
Faça um programa que informa o maior valor em uma lista sem utilizar a função max().
'''

lista = [23, 75, 234, 856, 12, 867, 244, 24]

maior = lista[0]

for elemento in lista:
    if elemento > maior:
        maior = elemento

print(maior)

