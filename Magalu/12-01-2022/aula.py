
"""
# exercício 01
print('Olá, mundo!')

# exercício 02
n = input('Informe um número: ')
print('O número informado foi', n)

# exercício 03
n = input('Informe um número: ')
n = float(n)
print(n)
n = int(n)
print(n)

# exercício 04
n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
print('A soma dos números é: ', n1+n2)

# exercício 05
n1 = float(input('Informe a nota do primeiro bimestre: '))
n2 = float(input('Informe a nota do segundo bimestre: '))
n3 = float(input('Informe a nota do terceiro bimestre: '))
n4 = float(input('Informe a nota do quarto bimestre: '))
print('A média é: ', (n1+n2+n3+n4)/4)

# exercício 06
r = float(input('Informe o raio do círculo: '))
area = 3.14*(r**2)
print('A área do círculo é de',area,'m2')

# exercício 07
salarioHora = float(input('Qual o seu salário hora: '))
horasMes = int(input('Número de horas trabalhadas no mês: '))
print('Seu salário mensal será de R$',salarioHora*horasMes)

# exercício 08
F = float(input('Qual a temperatura em Graus Fahrenheit: '))
C = (5 * (F-32) / 9)
print('A temperatura em Graus Celsius é de',C,'°C')
C = float(input('Qual a temperatura em Graus Celsius: '))
F = (C * (9/5)) + 32
print('A temperatura em Graus Fahrenheit é de',F,'°F')

# exercício 09
d = int(input('Informe o dia: '))
m = int(input('Informe o mês: '))
a = int(input('Informe o ano: '))
print('A data é',str(d)+'/'+str(m)+'/'+str(a))

# exercício 10
i1 = int(input('Informe o primeiro número inteiro: '))
i2 = int(input('Informe o segundo número inteiro: '))
r = float(input('Informe um número real: '))
print('o produto do dobro do primeiro com metade do segundo é',(i1*2)*(i2/2))
print('a soma do triplo do primeiro com o terceiro é',(i1*3)+r)
print(' o terceiro elevado ao cubo é',r**3)

# exercício 11
peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))
print('Seu IMC (índice de massa córporea) é de',peso/(altura**2))

# exercício 12
valor = float(input('Informe um valor em R$ '))
print('O novo valor é',valor*1.15)

# exercício 13
valor = float(input('Informe um valor em R$ '))
print('O novo valor é',valor*0.85)

# exercício 14
# fórmula para cálculo da posição: y(t) = y(0) + v(0)*t + (g*(t**2)/2) 
v0 = float(input('Informe a velocidade inicial (m/s): '))
p0 = float(input('Informe a posição inicial do objeto (m): '))
t1 = float(input('Informe o tempo em segundos: '))
print('A posição do objeto é',p0+(v0*t1)+(-10*(t1**2)/2))
"""
# exercício 15
from datetime import datetime
print(datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
