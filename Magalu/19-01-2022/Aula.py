"""
#exercício 01
lista = ['Helldanio','Muniz','Barros']
for x in range(len(lista)):
    print(lista[x])

#exercício 02
#comparando com o exercício 01, tivemos que utilizar 2 linhas a mais de código para obter o mesmo resultado.
lista = ['Helldanio','Muniz','Barros']
x = 0
while x < len(lista):
    print(lista[x])
    x += 1

#exercício 03
n = int(input('Informe um número: '))
lista = []
for x in range(n):
    lista.append(x)
print(lista)

#exercício 04
lista = [1,2,3,4,5,6,7,8,9,10]
pares = []
for x in range(len(lista)):
    if (lista[x] % 2) == 0:
        pares.append(lista[x])
print('Quantidade de números pares é:',len(pares))

#exercício 05
lista = [1,10,9,8,7,6,5,4,3,2]
lista.sort(reverse=True)
print('O maior número é:',lista[0])

#exercício 06
lista = [1,10,9,8,7,6,5,4,3,2]
print('Os três maiores números são:')
print(max(lista))
lista.remove(max(lista))
print(max(lista))
lista.remove(max(lista))
print(max(lista))

#exercício 07
lista1 = [1, 4, 5]
lista2 = [2, 2, 3]
lsoma = []
for x in range(len(lista1)):
    lsoma.append(lista1[x]+lista2[x])
print(lsoma)

#exercício 08
lista = []
for x in range(5):
    lista.append(input('Informe o número '+str(x+1)+' '))
print(lista)

#exercício 09
lista = []
for x in range(5):
    lista.append(input('Informe o número '+str(x+1)+' '))
print(lista)
for z in range(len(lista)):
    lista[z] = float(lista[z])
print(lista)

#exercício 10
notas = [0,0,0,0]
for x in range(len(notas)):
    notas[x] = float(input('Informe a nota do '+str(x)+'° bimestre: '))
print('A média é: ',sum(notas)/len(notas))

#exercício 11
lista = [1,2,3,4,5,6,7,8,9,10]
print(lista[:4])
print(lista[5:])
pares = []
impares = []
for x in range(len(lista)):
    if (lista[x] % 2) == 0:
        pares.append(lista[x])
    else:
        impares.append(lista[x])
print('Pares: ',pares)
print('Ímpares: ',impares)
lista.sort(reverse=True)
print(lista)
print(lista[5:])
print(lista[:5])

#exercício 12
import random
numeros = []
for x in range(10):
    numeros.append(random.randint(0,100))
maiorque50 = 0
for w in range(len(numeros)):
    if numeros[w]>50: maiorque50 += 1
print(numeros)
print('Temos',maiorque50,'números maiores que 50')

#exercício 13
import random
numeros = []
for x in range(10):
    numeros.append(random.randint(0,100))
print('Números sorteados:',numeros)
numeros.sort()
print('O maior número sorteado é:',numeros[9])
print('O menor número sorteado é:',numeros[0])
print('A média dos números sorteados é:',sum(numeros)/len(numeros))
print('A soma dos números sorteados é:',sum(numeros))
"""
#exercício 14
s_cpf = input('Informe o CPF: ')
cpf = []
for x in list(s_cpf):
    if x.isdigit() == False:
        print('Caractere inválido!')
        break
    else: cpf.append(x)
if len(cpf) != 11:
    print('O tamanho do CPF está incorreto!')
elif cpf == cpf[::-1]: #todos os números são iguais
    print('CPF inválido!')
else:
    n = 10
    resultado = 0
    for w in range(9):
        resultado += int(cpf[w])*n
        n -= 1
    dig1 = (resultado*10)%11
    if dig1 == 10: dig1 = 0
    n = 11
    resultado = 0
    for w in range(10):
        resultado += int(cpf[w])*n
        n -= 1
    dig2 = (resultado*10)%11
    if dig2 == 10: dig2 = 0
    if dig1 != int(cpf[9]) or dig2 != int(cpf[10]):
        print('CPF inválido!')
    else:
        print('O CPF está correto!')
