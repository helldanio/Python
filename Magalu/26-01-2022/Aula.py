"""
#exercício 01
def dobro(numero):
    print(numero*2)

dobro(2)

#exercício 02
def circunferencia(numero):
    return(2 * 3.1416 * numero)

raio = float(input('Informe o raio da circunferência: '))
print(f'O comprimento da circunferência é de {circunferencia(raio)}')

#exercício 03
def soma(n1,n2):
    return(n1+n2)

def subtracao(n1,n2):
    return(n1-n2)

def multiplicacao(n1,n2):
    return(n1*n2)

def divisao(n1,n2):
    return(n1/n2)

num1 = float(input('Informe o primeiro número: '))
num2 = float(input('Informe o segundo número: '))

print(f'A soma dos números é {soma(num1,num2)}')
print(f'A subtração dos números é {subtracao(num1,num2)}')
print(f'A multiplicação dos números é {multiplicacao(num1,num2)}')
print(f'A divisão dos números é {divisao(num1,num2)}')

#exercício 04
def ola(nome):
    print(f'Olá, {nome}')

print(ola('Helldânio'))

#exercício 05
def saudacao(nome, horario):
    if horario < '12:00': print(f'Bom dia, {nome}')
    elif '12:00' <= horario < '18:00': print(f'Boa tarde, {nome}')
    elif horario > '18:00': print(f'Boa noite, {nome}')

saudacao('Helldânio','20:55')

#exercício 06
def numeropar(numero):
    if numero%2 == 0: return(True)
    else: return(False)

#exercício 07
from random import randint

def sorteio():
    numeros = []
    for x in range(10):
        numeros.append(randint(0,100))
    return(max(numeros))

#exercício 07
from random import randint

def sorteio_media(n):
    numeros = []
    for x in range(n):
        numeros.append(randint(0,100))
    return(sum(numeros)/len(numeros))

#exercício 09
def caixa_alta(lista):
    for x in range(len(lista)):
        lista[x] = lista[x].upper()
    return(lista)

#exercício 10
def soma_listas(lista1,lista2):
    w = [x+y for x, y in zip(lista1,lista2)]
    return(w)

l1 = [1,2,3]
l2 = [4,5,6]
print(soma_listas(l1,l2))

#exercício 11
def multiplica_lista(numero,lista):
    w = [numero*y for y in lista]
    return(w)

l2 = [4,5,6]
print(multiplica_lista(2,l2))

#exercício 12
def produto_listas(lista1,lista2):
    w = [x*y for x, y in zip(lista1,lista2)]
    return(w)

l1 = [1,2,3]
l2 = [4,5,6]
print(produto_listas(l1,l2))

#exercício 13
def soma_lista(lista):
    return(sum(lista))

l1 = [1,2,3]
print(soma_lista(l1))

#exercício 14
def media_lista(lista):
    return(sum(lista)/len(lista))

l1 = [1,2,3]
print(media_lista(l1))

#exercício 15
def fatorial(num):
    if num == 0 or num == 1: return(1)
    nfat = num
    for x in range(num,1,-1):
        nfat *= (x-1)
    return(nfat)

print(fatorial(10))

#exercício 16
def fibonacci(termo):
    resultado = (1.618034**termo)-(1-1.618034)**termo
    resultado = int(resultado/(5**0.5))
    return(resultado)

for x in range(99):
    print(fibonacci(x))

print(fibonacci(10))

#exercício 17
def fatorial(num):
    if num == 0 or num == 1:
        return(1)
    else:
        return(num*fatorial(num-1))

print(fatorial(10))

#exercício 18
def verifica(dado,tipo):
    if tipo == 'idade':
        if 0 > dado > 150: return(False)
    elif tipo == 'salário':
        if dado <= 0: return(False)
    elif tipo == 'sexo':
        if dado not in ['M','F','O']: return(False)

#exercício 19
def fibonacci(termo):
    resultado = 0
    if termo == 1 or termo == 2: return(1)
    resultado = fibonacci(termo-1) + fibonacci(termo-2)
    return(resultado)

print(fibonacci(6))


#exercício 21
def clientes_incluir():
    nome = input('Informe o nome: ')
    cpf = input('Informe o CPF: ')
    email = input('Informe o e-mail: ')
    if len(buscar_cpf(cpf)) > 0:
        print('Cliente com CPF já cadastrado! Tecle Algo.')
        input()
    else:
        return([nome,cpf,email])

def clientes_buscar():
    cpf = input('Informe o CPF a consultar: ')
    cliente = buscar_cpf(cpf)
    if len(cliente) > 0:
        print('Cliente encontrado:')
        print(f'Nome: {cliente[0]} - CPF: {cliente[1]} - E-mail: {cliente[2]}')
        print('Tecle Algo.')
        input()
    else:
        print('Cliente não encontrado! Tecle Algo.')
        input()

def buscar_cpf(ncpf):
    cliente = []
    for x in range(len(clientes)):
        if ncpf == clientes[x][1]:
            cliente = clientes[x]
            break
    return cliente

def clientes_listar():
    print('LISTAGEM DE CLIENTES')
    print('-----------------------------------------------------')
    print('NOME                   CPF               E-MAIL')
    print('-----------------------------------------------------')
    for x in range(len(clientes)):
        print(f'{clientes[x][0]}  {clientes[x][1]}  {clientes[x][2]}')


def clientes_menu():
    print('----------------------------------------')
    print('    SISTEMA DE CADASTRO DE CLIENTES')
    print('----------------------------------------')
    print('1. Cadastrar novo cliente')
    print('2. Buscar cliente por CPF')
    print('3. Imprimir clientes')
    print('0. Sair do sistema')
    print()
    return(int(input('Digite sua opção: ')))

# PROGRAMA PRINCIPAL
opcao = 9
clientes = []
while opcao != 0:
    opcao = clientes_menu()
    
    if opcao == 1: 
        clientes.append(clientes_incluir())

    if opcao == 2:
        clientes_buscar()
    
    if opcao == 3:
        clientes_listar()

    if opcao == 0:
        print('Sistema Finalizado!')
"""
#exercício 20
import random

# GERAR BARALHO
def baralho_cria():
    '''
    O.Ouro
    C.Copas
    E.Espada
    P.Paus
    '''
    for x in range(4):  #definindo os naipes
        for y in range(13): #definindo as cartas para cada naipe
            if x == 0:
                baralho.append(['O'+str(y+1),y+1])
            elif x == 1:
                baralho.append(['C'+str(y+1),y+1])
            elif x == 2:
                baralho.append(['E'+str(y+1),y+1])
            elif x == 3:
                baralho.append(['P'+str(y+1),y+1])

def escolher_carta():
    # Se o baralho tiver mais de uma carta, a função escolherá aleatoriamente uma delas, caso contrário retorna
    # a carta que sobrou. Após a escolha, a carta é retirada do baralho.
    if len(baralho) > 1:
        numero = random.randint(0,len(baralho)-1)  # o termo da lista inicia em 0 e termina em 51, por isso "len(baralho)-1"
    else:
        if len(baralho) == 1:
            numero = 0
        else:
            print('O baralho não possui mais cartas disponíveis!')
            for w in range(len(jogadores)):
                jogadores[w][2] = False
            return('FIM')
    carta = baralho[numero]
    baralho.remove(carta)
    return(carta)

def verifica_ganhador(x_jogadores):
    x_jogadores = sorted(x_jogadores, key=lambda x: x[1], reverse=True)  #ordenando a lista em ordem decrescente de pontos
    print('-----------------------------')
    print('    PLACAR FINAL DO JOGO')
    print('-----------------------------')
    for x in range(len(x_jogadores)):
        print(f'{x_jogadores[x][0]} - Pontos: {x_jogadores[x][1]}')
        if x_jogadores[x][0] == 'Computador':
            print('     Cartas escolhidas pelo Computador:')
            print('     ----------------------------------')
            for w in range(len(jogadores_carta)):
                if jogadores_carta[w][0] == 'Computador':
                    identifica_carta(jogadores_carta[w][1],1)
        print('-----------------------------')
    print()
    for w in range(len(x_jogadores)):
        if x_jogadores[w][1] <= 21:   #o primeiro jogador encontrado com 21 ou imediatamente menor é declarado vencedor 
            print('O ganhador é: ',x_jogadores[w][0],'com',x_jogadores[w][1],'pontos')
            break  

def identifica_carta(carta,modo=0):
    nome_carta = ''
    tipo_carta = ''
    numero_carta = int(carta[1:])
    if numero_carta == 1: nome_carta = 'ÁS'
    if numero_carta == 2: nome_carta = 'Dois'
    if numero_carta == 3: nome_carta = 'Três'
    if numero_carta == 4: nome_carta = 'Quatro'
    if numero_carta == 5: nome_carta = 'Cinco'
    if numero_carta == 6: nome_carta = 'Seis'
    if numero_carta == 7: nome_carta = 'Sete'
    if numero_carta == 8: nome_carta = 'Oito'
    if numero_carta == 9: nome_carta = 'Nove'
    if numero_carta == 10: nome_carta = 'Dez'
    if numero_carta == 11: nome_carta = 'Valete'
    if numero_carta == 12: nome_carta = 'Dama'
    if numero_carta == 13: nome_carta = 'Reis'
    if carta[0] == 'O': tipo_carta = 'Ouro'
    elif carta[0] == 'C': tipo_carta = 'Copas'
    elif carta[0] == 'E': tipo_carta = 'Espadas'
    elif carta[0] == 'P': tipo_carta = 'Paus'
    if modo == 0:
        print('A carta é:',nome_carta,'de',tipo_carta)
    else:
        print('     ',nome_carta,'de',tipo_carta)

def computador_joga():  # ESTA FUNCAO FARÁ COM QUE O COMPUTADOR ESCOLHA UMA CARTA DENTRO DA PROBABILIDADE DE 50% DE CHANCES DE NÃO ESTOURAR A PONTUAÇÃO
    while jogadores[0][1] <= 21:
        pontuacao = jogadores[0][1]
        carta = escolher_carta()
        if carta[1] > 10:  # SE O VALOR DA CARTA CORRESPONDER A 11, 12 OU 13 (DAMA, VALETE E REIS)
            pontuacao = 10
        else:
            pontuacao = carta[1]                
        jogadores[0][1] += pontuacao
        jogadores_carta.append([jogadores[0][0],carta[0],pontuacao])        
        if jogadores[0][1] > 21:
            jogadores[0][2] = False
        else:
            if jogadores[0][1] > 17: break # SE A PONTUAÇÃO ATUAL FOR MAIOR QUE 17 PONTOS, O COMPUTADOR PARA DE ARRISCAR.
            elif jogadores[0][1] > 11: # SE A PONTUAÇÃO FOR MAIOR QUE 11 PONTOS E A PENULTIMA CARTA ESCOLHIDA TIVER SIDO MENOR QUE 6, O COMPUTADOR PARA DE ARRISCAR.
                ultima_pontuacao = jogadores_carta[len(jogadores_carta)-1][2]
                if ultima_pontuacao < 6:
                    break
    jogadores[0][2] = False

def inicio():
    # o máximo de 5 apenas por questão de estratégia
    print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄')
    print('▓                   B L A C K   J A C K   2 1                     ▓')
    print('▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀')
    print("       By Helldânio Barros - CopyRight(2022) - Let's Code")
    print('-------------------------------------------------------------------')
    print('SE VOCÊ ESCOLHER APENAS 1 JOGADOR, O COMPUTADOR SERÁ SEU ADVERSÁRIO')
    print('Obs: O computador também arrisca e pode estourar a pontuação')
    print('-------------------------------------------------------------------')
    n_jogadores = 0
    while n_jogadores == 0:
        n_jogadores = input('Quantos jogadores (máximo 5): ')
        if n_jogadores.isdigit():
            n_jogadores = int(n_jogadores)
        else:
            n_jogadores = 0
    if n_jogadores > 5: return
    if n_jogadores == 1:
        jogadores.append(['Computador',0,True])
    for x in range(n_jogadores):
        # jogadores = [Nome,Pontuação,Status(True-Ativo False-Inativo)]
        jogadores.append([input(f'Informe o nome do jogador {x+1}: '),0,True])

    baralho_cria()

    if jogadores[0][0] == 'Computador':
        computador_joga()

    for w in range(len(jogadores)):
        while jogadores[w][2]:
            print(f'Sr.(a) {jogadores[w][0]} - sua pontuação é: {jogadores[w][1]}')
            if input('Deseja comprar uma carta?') in ['S','s']:                
                pontuacao = jogadores[w][1]
                carta = escolher_carta()
                if carta == 'FIM': break
                identifica_carta(carta[0])
                if carta[1] > 10:  # SE O VALOR DA CARTA CORRESPONDER A 11, 12 OU 13 (DAMA, VALETE E REIS)
                    pontuacao = 10
                else:
                    pontuacao = carta[1]                
                jogadores[w][1] += pontuacao
                jogadores_carta.append([jogadores[w][0],carta[0],pontuacao])
                if jogadores[w][1] > 21:
                    jogadores[w][2] = False
                    print(f'O jogador {jogadores[w][0]} está fora do jogo!')

            else:
                jogadores[w][2] = False
    
    verifica_ganhador(jogadores)

#Início do Programa Principal
vamos_jogar = 'S'
while vamos_jogar == 'S':
    jogadores = []
    jogadores_carta = []
    baralho = []
    inicio()
    vamos_jogar = input('Vamos jogar novamente?').upper()
#Fim.