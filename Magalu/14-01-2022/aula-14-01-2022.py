"""
# exercício 01
idade = int(input('Informe sua idade: '))
if idade > 17:
    print('Você é maior de 18 anos')
else:
    print('Você é menor de 18 anos')

# exercício 02
n = float(input('Informe um número: '))
if n < 0:
    print('Número negativo')
elif n > 0:
    print('Número positivo')
else:
    print('O número "0" é um número neutro, nem positivo e nem negativo')

# exercício 03
n1 = float(input('Informe o primeiro número: '))
n2 = float(input('Informe o segundo número: '))
if n1 < n2:
    print('O maior número é',n2)
elif n1 > n2:
    print('O maior número é',n1)
else:
    print('Os números são iguais')

# exercício 04
idade = int(input('Informe a sua idade: '))
salario = float(input('Informe seu salário: '))
sexo = input('Qual seu gênero (M/F/O): ')
if idade < 0 or idade > 150:
    print('Sua idade tem que estar entre 0 e 150')
if salario <= 0:
    print('Seu salário tem que ser maior que ZERO')
if sexo not in ['M','F','O']:
    print('Gênero inválido, digite M, F ou O')

# exercício 05
n1 = float(input('Informe a nota 1: '))
n2 = float(input('Informe a nota 2: '))
n3 = float(input('Informe a nota 3: '))
if (n1+n2+n3)/3 > 6:
    print('Você passou de ano!')
else:
    print('Infelizmente você foi reprovado.')

# exercício 06
resultado = 0
if input('Mora perto da vítima?') in ['S','s']: resultado += 1
if input('Já trabalhou com a vítima?') in ['S','s']: resultado += 1
if input('Telefonou para a vítima?') in ['S','s']: resultado += 1
if input('Esteve no local do crime?') in ['S','s']: resultado += 1
if input('Devia para a vítima?') in ['S','s']: resultado += 1
if resultado == 5:
    print('É um assassino!')
elif resultado >= 3:
    print('É um cúmplice!')
elif resultado == 2:
    print('É um suspeito!')
else:
    print('O suspeito está liberado!')

# exercício 07
resultado = ''
if input('Sente dor no corpo?') in ['S','s']: resultado += 'S'
else: resultado += 'N'
if input('Você tem febre?') in ['S','s']: resultado += 'S'
else: resultado += 'N'
if input('Você tem tosse?') in ['S','s']: resultado += 'S'
else: resultado += 'N'
if input('Está com congestão nasal?') in ['S','s']: resultado += 'S'
else: resultado += 'N'
if input('Tem manchas pelo corpo?') in ['S','s']: resultado += 'S'
else: resultado += 'N'
if resultado == 'SSNNS':
    print('Você está com DENGUE.')
elif resultado == 'SSSSN' or resultado == 'NSSSN':
    print('Você está com GRIPE.')
elif resultado == 'SNNNN' or resultado == 'NNNNN':
    print('Você não está doente.')
else:
    print('Não foi possível efetuar o diagnóstico!')

# exercício complementar 02
n1 = float(input('Informe o primeiro número: '))
n2 = float(input('Informe o segundo número: '))
n3 = float(input('Informe o terceiro número: '))
if n1 == n2 == n3:
    print('Os números são iguais.')
elif n2 <= n1 >= n3:
    print('O maior número é',n1)
elif n1 <= n2 >= n3:
    print('O maior número é',n2)
elif n1 <= n3 >= n2:
    print('O maior número é',n3)
"""
# exercício complementar 03
n1 = float(input('Informe o primeiro número: '))
n2 = float(input('Informe o segundo número: '))
n3 = float(input('Informe o terceiro número: '))
n4 = float(input('Informe o quarto número: '))
if n1 == n2 == n3 == n4:
    print('Os números são iguais.')
elif n2 <= n1 >= n3:
    if n4 > n1: print('O maior número é',n4)
    else: print('O maior número é',n1)
elif n1 <= n2 >= n3:
    if n4 > n2: print('O maior número é',n4)
    else: print('O maior número é',n2)
elif n1 <= n3 >= n2:
    if n4 > n3: print('O maior número é',n4)
    else: print('O maior número é',n3)
