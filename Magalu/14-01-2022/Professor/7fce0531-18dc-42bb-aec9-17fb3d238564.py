'''
Desafio 3 - Um hospital quer fazer o diagnóstico de gripe ou dengue a partir de um 
questionário de sintomas, tendo as perguntas abaixo, faça um programa que faça o 
diagnóstico deste hospital:

a. Sente dor no corpo?
b. Você tem febre?
c. Você tem tosse?
d. Está com congestão nasal?
e. Tem manchas pelo corpo?

Para o diagnóstico ele tem a seguinte tabela:
A	B	C	D	E	Resultado
Sim	Sim	Não	Não	Sim	Dengue
Sim	Sim	Sim	Sim	Não	Gripe
Não	Sim	Sim	Sim	Não	Gripe
Sim	Não	Não	Não	Não	Sem doenças
Não	Não	Não	Não	Não	Sem doenças
'''

a = input('Sente dor no corpo?')
b = input('Você tem febre?')
c = input('Você tem tosse?')
d = input('Está com congestão nasal?')
e = input('Tem manchas pelo corpo?')

# Sim	Sim	Não	Não	Sim	Dengue
if a == 's' and b == 's' and c != 's' and d != 's' and e == 's':
    print('Dengue')
# Sim	Sim	Sim	Sim	Não	Gripe
elif a == 's' and b == 's' and c == 's' and d == 's' and e != 's':
    print('Gripe')
# Não	Sim	Sim	Sim	Não	Gripe
elif a != 's' and b == 's' and c == 's' and d == 's' and e != 's':
    print('Gripe')
# Sim	Não	Não	Não	Não	Sem doenças
elif a == 's' and b != 's' and c != 's' and d != 's' and e != 's':
    print('Sem doenças')
# Não	Não	Não	Não	Não	Sem doenças
elif a != 's' and b != 's' and c != 's' and d != 's' and e != 's':
    print('Sem doenças')
else:
    print('Doença desconhecida.')