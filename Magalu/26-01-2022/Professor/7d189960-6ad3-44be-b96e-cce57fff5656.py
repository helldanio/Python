'''
Faça uma função que recebe um número e retorna True se ele é par ou False, 
se ele é ímpar.
'''

def par_ou_impar(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

# forma mais enxuta
def par_ou_impar2(numero):
    return numero % 2 == 0


##########
'''
num = int(input('Digite um número: '))
#print(par_ou_impar(num))
if par_ou_impar(num):
    print('Par')
else:
    print('Ímpar')
'''
'''
num = int(input('Digite um número: '))
resultado = par_ou_impar(num)
if resultado == True:
    print('Par')
else:
    print('Ímpar')
'''

'''
Faça uma função que sorteia 10 números aleatórios entre 0 e 100 e 
retorna o maior entre eles.
'''
import random

def maior10():
    sorteios = []
    for contador in range(10):
        sorteio = random.randint(0, 100)
        sorteios.append(sorteio)
    maior = max(sorteios)
    #print(sorteios)
    return maior

#print(maior10())

'''
Faça uma função que recebe uma lista de palavras e retorna uma lista 
contendo as mesmas palavras da lista anterior, porém escritas em caixa alta.
'''
# DICA:
string_original = 'oLá MuNdo!'

maiuscula = string_original.upper()
print(maiuscula)
minuscula = string_original.lower()
print(minuscula)
titulo = string_original.title()
print(titulo)
primeira_maiuscula = string_original.capitalize()
print(primeira_maiuscula)

print(string_original)

substituida = maiuscula.replace('O', '@')
print(substituida)