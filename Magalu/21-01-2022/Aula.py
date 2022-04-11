"""
#exercício 01
meses = {'Janeiro':31,'Fevereiro':28,'Março':31,'Abril':30,'Maio':31,'Junho':30,'Julho':31,'Agosto':31,'Setembro':30,'Outubro':31,'Novembro':30,'Dezembro':31}

#exercício 02
meses = {'Janeiro':31,'Fevereiro':28,'Março':31,'Abril':30,'Maio':31,'Junho':30,'Julho':31,'Agosto':31,'Setembro':30,'Outubro':31,'Novembro':30,'Dezembro':31}
for x in meses:
    print(x,'-',meses[x])

#exercício 03
frutas = {'Banana': 3.0,'Cebola': 4.0,'Maçã': 5.7,'Abacaxi': 8.0}

#exercício 04
frutas = {'Banana': 3.0,'Cebola': 4.0,'Maçã': 5.7,'Abacaxi': 8.0}
frutas.update({'Maçã':8.6})
print(frutas['Maçã'])
print(frutas)

#exercício 05
dados = {}
def grava(s_nome,n_idade,s_email):
    if 'nome' in dados:
        dados['nome'].append([s_nome])
    else:
        dados.update({'nome': [s_nome]})
    if 'idade' in dados:
        dados['idade'].append([n_idade])
    else:
        dados.update({'idade': [n_idade]})
    if 'email' in dados:
        dados['email'].append([s_email])
    else:
        dados.update({'email': [s_email]})

snome = 'inicio'
while snome != '':
    snome = input('Informe seu nome (ENTER p/ sair): ')
    if snome == '': break
    nidade = int(input('Informe sua idade: '))
    semail = input('Informe seu e-mail: ')
    grava(snome,nidade,semail)
print(dados)

#exercício 06
dados = {'item':{'nome':'Maria','a':1,'b':5},'item1':{'nome':'Pedro','a':0.5,'b':3},'item2':{'nome':'João','a':3.2,'b':1}}
print(dados['item1']['nome'],dados['item1']['b'])

#exercício 07
lista = ['carro','casa','casa','moto','uva','casa','carro','cachorro','gato','casa','cachorro','uva','moto','casa','gato']
elementos = {}
for x in range(len(lista)):
    if lista[x] in elementos:
        qtd = elementos[lista[x]]+1      
    else:
        qtd = 1
    elementos.update({lista[x]:qtd})
print(elementos)

#exercício 08
print('--------------------------------')
print('     CADASTRO DE USUÁRIOS')
print('--------------------------------')
print('1. Cadastrar novo usuário')
print('2. Imprimir usuários')
print('3. Sair do sistema')
opcao = 0
usuarios = {}
while opcao != 3:
    opcao = int(input('Escolha uma opção: '))
    if opcao == 1:
        cpf = input('Informe o cpf: ')
        if cpf in usuarios:
            print('CPF já cadastrado')
        else:
            nome = input('Informe o nome: ')
            idade = int(input('Informe sua idade: '))
            email = input('Informe o e-mail: ')
            usuarios.update({cpf:{'nome':nome,'idade':idade,'email':email}})
    elif opcao == 2:
        for x, y in usuarios.items():
            print(f'Dados para o Cpf {x}')
            for n, m in y.items():
                print(f'o(a) {n} é {m}')
"""
#exercício 09
print('--------------------------------')
print('     CADASTRO DE USUÁRIOS')
print('--------------------------------')
print('1. Cadastrar novo usuário')
print('2. Imprimir usuários')
print('3. Buscar Usuário')
print('4. Sair do sistema')
opcao = 0
usuarios = {}
while opcao != 4:
    opcao = int(input('Escolha uma opção: '))
    if opcao == 1:
        cpf = input('Informe o cpf: ')
        if cpf in usuarios:
            print('CPF já cadastrado')
        else:
            nome = input('Informe o nome: ')
            idade = int(input('Informe sua idade: '))
            email = input('Informe o e-mail: ')
            usuarios.update({cpf:{'nome':nome,'idade':idade,'email':email}})
    elif opcao == 2:
        for x, y in usuarios.items():
            print(f'Dados para o Cpf {x}')
            for n, m in y.items():
                print(f'o(a) {n} é {m}')
    elif opcao == 3:
        busca = input('Informe o CPF a consultar: ')
        if busca not in usuarios:
            print('O CPF buscado não está cadastrado!')
        else:
            print('DADOS DO USUÁRIO')
            print('----------------')
            for x, y in usuarios[busca].items():
                print(f'{x} = {y}')
