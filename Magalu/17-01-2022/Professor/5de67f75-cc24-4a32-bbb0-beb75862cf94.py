# Pergunte ao usuário a quantidade de provas que ele fez.
# Calcule e exiba sua média aritmética (pode "perder" valores já digitados).

quantidade = int(input('Digite a quantidade de provas: '))
soma = 0

contador = 1
while contador <= quantidade:
    nota = float(input('Digite a sua nota: '))
    soma = soma + nota
    contador = contador + 1
media = soma/quantidade
print(media)

'''
contador = 1
quantidade = 3

nota     soma
7        7
9        16
10       26

'''


'''
contador = 1

limite = int(input('Digite o número máximo: '))

while contador <= limite:
    print(contador)
    contador = contador + 1
'''

'''
idade = int(input('Digite a idade: '))

while idade < 0 or idade > 150:
    print('Erro!')
    idade = int(input('Digite outra idade: '))

print('Idade ok:', idade)
'''