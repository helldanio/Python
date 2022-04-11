# Validar se o sexo do usuário é igual a M, F ou Outro

idade = int(input('Digite a sua idade: '))
salario = float(input('Digite o seu salário: '))
sexo = input('Digite o seu sexo: ')

'''
if sexo != 'M' and sexo != 'F' and sexo != 'Outro':
    print('Sexo inválido')
else:
    print('Sexo válido')
'''

if sexo == 'M' or sexo == 'F' or sexo == 'Outro':
    print('Sexo válido')
else:
    print('Sexo inválido')