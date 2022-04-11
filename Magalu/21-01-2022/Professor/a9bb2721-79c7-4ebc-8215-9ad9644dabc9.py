'''
Crie um dicionário cujas chaves são os meses do ano e os valores são a duração (em dias) 
de cada mês.
'''
meses = {   'Janeiro':31,
            'Fevereiro': 28,
            'Março': 31,
            'Abril':30
        }

print(meses)

'''
Imprima as chaves seguidas dos seus valores para dicionário criado no exercício anterior.
'''

# Dica: for em dicionário percorre chaves
# Dica 2: se temos a chave, podemos obter o valor

for chave in meses:
    print(chave, '-', meses[chave])

meses['Fevereiro'] = 29

print(meses)

dicionario = {
    '123.456.789-12' : {'nome':'Rafael', 'email':'rafael@letscode.com.br'},
    '987.654.321-98' : {'nome':'Matheus', 'email':'matheus@letscode.com.br'},
}

print(dicionario['123.456.789-12']['email'])