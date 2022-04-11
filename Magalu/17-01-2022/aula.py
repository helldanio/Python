"""
# exercício 01
n = int(input('Informe um número: '))
contador = 1
while contador <= n:
    print(contador)
    contador += 1

# exercício 02
n = int(input('Informe um número para fatorial: '))
if n <= 0:
    print('Não pode ser ZERO')
elif n == 1:
    print('Fatorial é igual a 1')
else:
    resultado = n*(n-1)
    n -= 1
    while n > 1:
        n -= 1
        resultado += resultado*(n-1)
        
    print('Resultado do fatorial é',resultado)

# exercício 03
n = int(input('Informe um número: '))
if n < 1:
    print('Número inválido!')
else:    
    contador = 1
    resultado = 0
    while contador <= n:
        resultado += contador
        contador += 1
    print('O resultado da soma é:',resultado)

# exercício 04
n = 9
i = 1
while i <= 10:
    print('9 x',i,'=',n*i)
    i += 1

# exercício 05
n = 1
resultado = 0
while n != 0:
    n = int(input('Informe um número (0 para finalizar): '))
    if n > 0:
        resultado += n
print('O resultado da soma é:',resultado)

# exercício 06
import random
n = random.randint(1,10)
r = 0
print('SORTEAMOS UM NÚMERO ENTRE 1 E 10, ESCOLHA O NÚMERO')
print('--------------------------------------------------')
while r != n:
    r = int(input('Informe um número (0 para desistir): '))
    if r == n or r == 0:
        if r == 0:
            print('Fim!')
            break
        else:
            print('Parabéns!!! Você acertou.')
    else:
        print('Você errou! Digite novamente.')

# exercício 07
idade = 151
while idade < 0 or idade > 150:
    idade = int(input('Informe a sua idade (0-150): '))

salario = 0
while salario <= 0:
    salario = float(input('Informe seu salário (maior que ZERO): '))

sexo = 'X'
while sexo not in ['M','F','O']:
    sexo = input('Qual seu gênero (M/F/O): ')

# exercício 08
n = 1
r = 1
resultado = 0
while n < 1000:
    resultado += r
    r = r/2
    n += 1
print('O resultado da soma dos termos é',resultado)
"""
# exercício 09
def fatorial(x):
    if x == 0 or x == 1: return 1
    res = x*(x-1)
    x -= 1
    while x > 1:
        x -= 1
        res += res*(x-1)
    return res

n = 1
r = 1
resultado = 0
while n < 1000:
    resultado += r/fatorial(n)
    n += 1
print('O resultado é',resultado)
