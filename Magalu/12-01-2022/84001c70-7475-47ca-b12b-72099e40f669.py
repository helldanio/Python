# comentário é ignorado pelo python!

'''
inteiro (int) - 1, 2, 10, 30, 100, 1000, -5, -10
real (float) - 3.14, 2.7, -5.7, 2.99, 1.0, 5.0
texto/literal/string (str) "olá mundo", 'Magalu desenvolve 40+'
booleano/lógico (bool) - True, False
'''

# Pergunte pro usuário o seu nome, a sua idade e responda há quanto tempo
# ele estava habilitado a participar do programa Magalu Desenvolve 40+

nota_final = 10.0
nome = input('Digite o seu nome: ')
idade = int(input('Digite a sua idade: '))

tempo = idade - 40

print('O(a) aluno(a)', nome, 'pode participar há', tempo, 'anos')

'''
Operações aritméticas
+ soma
- subtração
* multiplicação
/ divisão real
// divisão inteira
% resto da divisão

 9 | 2
-8    4.5   ----> divisão real (9/2)
---
 10
-10
---
0

 9 | 2
-8    4 -----> divisão inteira (9//2)
---
 1 ----------> resto da divisão (9%2)
** potência
'''

'''
Desafio 1 - Peça para o usuário digitar uma velocidade inicial (em m/s), uma 
posição inicial (em m) e um instante de tempo (em s) e imprima a posição de um 
projétil nesse instante de tempo.

Use a fórmula matemática:

y(t) = y(0) + v(0)*t + (g*(t**2)/2)

Onde, g é a aceleração da gravidade (-10m/s²), y(t) é a posição final, y(0) 
é a posição inicial, v(0) é a velocidade inicial e t é o instante de tempo.
'''
velocidade_inicial = float(input('Digite a velocidade inicial: '))
posicao_inicial = float(input('Digite a posição inicial: '))
tempo = float(input('Digite o instante de tempo: '))
g = -10 # aceleração gravitacional

posicao = posicao_inicial + velocidade_inicial*tempo + (g*(tempo**2)/2)

print(posicao, "m")
