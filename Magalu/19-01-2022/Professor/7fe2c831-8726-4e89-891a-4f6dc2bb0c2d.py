notas = []

quantidade = int(input('Digite a quantidade de provas: '))

# esse loop NÃO É para percorrer lista!
# esse loop é para repetir operações (leitura de nota)
for contador in range(quantidade):
    nota = float(input('Digite a sua nota: '))
    notas.append(nota)

# o próximo loop VAI percorrer a lista:
soma = 0
for n in notas:
    soma = soma + n
media = soma/len(notas)
# media = soma/quantidade

maior = max(notas)
menor = min(notas)

print('Sua média foi:', media)
print('Maior nota:', maior)
print('Menor nota:', menor)

#################################
# outras observações:

notas.append(10) # insere o valor 10 no final da lista
notas.remove(5)  # remove o valor 5 da lista

notas.insert(7, 10) # insere o valor 10 na posição 7
notas.pop(5)        # remove o elemento que estiver na posição 5

if 10 in notas:
    print('existe nota 10')