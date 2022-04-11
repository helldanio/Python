'''
Faça um programa que sorteia um número N e peça para o usuário adivinhar o número sorteado. 
A cada resposta errada, o seu programa deve imprimir um aviso dizendo que a resposta está 
errada e pedir novamente uma resposta ao usuário.

Para a realização desse exercício, utilize alguma função da biblioteca random 
(e.g. randint()).
'''
import random

sorteio = random.randint(1, 10)

palpite = 0 
tentativas = 0

while palpite != sorteio:
    palpite = int(input('Digite um número: '))
    tentativas = tentativas + 1

print('Parabéns! O número sorteado foi:', sorteio)
print('O número de tentativas foi: ', tentativas)

'''
1 + 1/2 + 1/4 + ... = 2.0
1/1! + 1/2! + 1/3! + ... = 1.718
'''