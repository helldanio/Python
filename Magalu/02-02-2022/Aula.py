'''
#exercício 01
class Bola:

    def __init__(self, cor, raio):
        self.cor = cor
        self.raio = raio

    def cor(self):
        return(self.cor)

    def area(self):     
        ar = 4*3.14*self.raio*self.raio
        return(ar)

    def volume(self):
        vol = 4*3.14*self.raio*self.raio*self.raio/3
        return(vol)

    def __repr__(self):
        return(f'A bola é {self.cor} e tem raio {self.raio}')

nova_bola = Bola('azul',6)
print(nova_bola.cor)
print(nova_bola.area())
print(nova_bola.volume())

#exercício 02
class Retangulo:

    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b

    def area(self):
        return(self.lado_a*self.lado_b)

    def __repr__(self):
        return(f'Os lados do retângulo são {self.lado_a} e {self.lado_b}')

ret1 = Retangulo(5,6)
print(f'A área do retângulo é de {ret1.area()} cm2')


#exercício 03
class Funcionario:

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def salario_mensal(self):
        salario_mensal = horas_trabalhadas['fevereiro']*salario_hora['fevereiro']
        return(salario_mensal)

    def __repr__(self):
        return(f'O nome do funcionário é: {self.nome} e seu e-mail: {self.email}')


horas_trabalhadas = {'fevereiro':220}
salario_hora = {'fevereiro':20}

Func1 = Funcionario('José da Silva','josedasilva@ponto.com')
salario = Func1.salario_mensal()
print(f'O Salário mensal de {Func1.nome} é de R$ {salario:.2f} reais.')

#exercício 04
class Televisor:

    def __init__(self, fabricante, modelo, canal_atual, lista_canais, volume):
        self.fabricante = fabricante
        self.modelo = modelo
        self.canal_atual = canal_atual
        self.lista_canais = lista_canais
        self.volume = volume

    def aumenta_volume(self):
        if self.volume < 100:
            self.volume += 1

    def diminui_volume(self):
        if self.volume > 0:
            self.volume -= 1

    def trocar_canal(self, novo_canal):
        if novo_canal in self.lista_canais:
            self.canal_atual = novo_canal

    def adiciona_canal(self, novo_canal):
        if novo_canal not in self.lista_canais:
            self.lista_canais.append(novo_canal)

    def __repr__(self):
        return(f'A TV modelo {self.modelo} foi fabricada por {self.fabricante}')


#exercício 05
class ControleRemoto:

    def __init__(self, televisao):
        self.televisao = televisao

    def aumenta_volume(self):
        self.televisao.aumenta_volume()

    def diminui_volume(self):
        self.televisao.diminui_volume()

    def trocar_canal(self, novo_canal):
        self.televisao.trocar_canal(novo_canal)

    def adiciona_canal(self, novo_canal):
        self.televisao.adiciona_canal(novo_canal)

tv = Televisor('SAMSUNG','H65',4,[4,5,7,12,16],25)
cr = ControleRemoto(tv)
cr.trocar_canal(5)
cr.aumenta_volume()
cr.diminui_volume()
cr.adiciona_canal(18)
print(tv.lista_canais)

#exercício 06
import time

class Cronometro:

    def __init__(self, tempo):
        self.tempo = tempo
        
    def inicia(self):
        if self.tempo < 1: self.tempo = 1
        if self.tempo > 59: self.tempo = 59
        self.imprime()

    def imprime(self):

        n = []
        i = []
        for x in range(10):
            for w in range(7):
                i.append('')
            n.append(i)
            i = []

        n[0][0] = ''
        n[0][1] = '▓▓▓▓▓▓▓▓'
        n[0][2] = '▓▓    ▓▓'
        n[0][3] = '▓▓    ▓▓'
        n[0][4] = '▓▓    ▓▓'
        n[0][5] = '▓▓    ▓▓'
        n[0][6] = '▓▓▓▓▓▓▓▓'

        n[1][0] = ''
        n[1][1] = '  ▓▓▓▓  '
        n[1][2] = '▓▓  ▓▓  '
        n[1][3] = '    ▓▓  '
        n[1][4] = '    ▓▓  '
        n[1][5] = '    ▓▓  '
        n[1][6] = ' ▓▓▓▓▓▓▓'

        n[2][0] = ''
        n[2][1] = '▓▓▓▓▓▓▓▓'
        n[2][2] = '      ▓▓'
        n[2][3] = '      ▓▓'
        n[2][4] = '▓▓▓▓▓▓▓▓'
        n[2][5] = '▓▓      '
        n[2][6] = '▓▓▓▓▓▓▓▓'

        n[3][0] = ''
        n[3][1] = '▓▓▓▓▓▓▓▓'
        n[3][2] = '      ▓▓'
        n[3][3] = '      ▓▓'
        n[3][4] = '▓▓▓▓▓▓▓▓'
        n[3][5] = '      ▓▓'
        n[3][6] = '▓▓▓▓▓▓▓▓'

        n[4][0] = ''
        n[4][1] = '▓▓    ▓▓'
        n[4][2] = '▓▓    ▓▓'
        n[4][3] = '▓▓▓▓▓▓▓▓'
        n[4][4] = '      ▓▓'
        n[4][5] = '      ▓▓'
        n[4][6] = '      ▓▓'

        n[5][0] = ''
        n[5][1] = '▓▓▓▓▓▓▓▓'
        n[5][2] = '▓▓      '
        n[5][3] = '▓▓      '
        n[5][4] = '▓▓▓▓▓▓▓▓'
        n[5][5] = '      ▓▓'
        n[5][6] = '▓▓▓▓▓▓▓▓'

        n[6][0] = ''
        n[6][1] = '   ▓▓▓▓▓'
        n[6][2] = ' ▓▓     '
        n[6][3] = '▓▓      '
        n[6][4] = '▓▓▓▓▓▓▓▓'
        n[6][5] = '▓▓    ▓▓'
        n[6][6] = '▓▓▓▓▓▓▓▓'

        n[7][0] = ''
        n[7][1] = '▓▓▓▓▓▓▓▓'
        n[7][2] = '      ▓▓'
        n[7][3] = '     ▓▓ '
        n[7][4] = '    ▓▓  '
        n[7][5] = '   ▓▓   '
        n[7][6] = '   ▓▓   '

        n[8][0] = ''
        n[8][1] = '▓▓▓▓▓▓▓▓'
        n[8][2] = '▓▓    ▓▓'
        n[8][3] = '▓▓    ▓▓'
        n[8][4] = '▓▓▓▓▓▓▓▓'
        n[8][5] = '▓▓    ▓▓'
        n[8][6] = '▓▓▓▓▓▓▓▓'

        n[9][0] = ''
        n[9][1] = '▓▓▓▓▓▓▓▓'
        n[9][2] = '▓▓    ▓▓'
        n[9][3] = '▓▓    ▓▓'
        n[9][4] = '▓▓▓▓▓▓▓▓'
        n[9][5] = '      ▓▓'
        n[9][6] = '▓▓▓▓▓▓▓▓'

        for x in range(self.tempo+1):
            sTempo = str(x)
            print( '\n' * 130)
            n1 = int(sTempo[0])            
            if len(sTempo) > 1: n2 = int(sTempo[1])
            print(n[n1][1],n[n2][1] if len(sTempo) > 1 else '')
            print(n[n1][2],n[n2][2] if len(sTempo) > 1 else '')
            print(n[n1][3],n[n2][3] if len(sTempo) > 1 else '')
            print(n[n1][4],n[n2][4] if len(sTempo) > 1 else '')
            print(n[n1][5],n[n2][5] if len(sTempo) > 1 else '')
            print(n[n1][6],n[n2][6] if len(sTempo) > 1 else '')
            time.sleep(1)

    def __repr__(self):
        return(f'O cronômetro contabilizará {self.tempo} segundos.')

     
#cronômentro de segundos, informar um número de 1 a 59
relogio = Cronometro(25)
relogio.inicia()

#exercício 07
class Agenda:

    def __init__(self, dados):
        self.dados = dados

    def incluir(self, nome, endereco, email, telefone):
        inclui = True
        if len(self.dados) > 0:
            for x in self.dados:
                if nome == x[0]:
                    inclui = False
        if inclui:
            self.dados.append([nome,endereco,email,telefone])
        else:
            print('Cadastro já efetivado!')

    def remover(self, nome):
        for x in self.dados:
            if nome == x[0]:
                self.dados.remove(x)
    
    def buscar(self, nome):
        for x in self.dados:
            if nome == x[0]:
                print(x)

    def listar(self):
        for x in self.dados:
            print(x)
    
dados_agenda = []
nova_agenda = Agenda(dados_agenda)
nova_agenda.incluir('Helldanio','Rua Lucilio','helldanio@gmail.com','(86) 99885740')
nova_agenda.incluir('Luzinete','Rua Albuquerque','luzinetelimabarros@gmail.com','(86) 9999999999')
nova_agenda.incluir('Helldanio','Rua Lucilio','helldanio@gmail.com','(86) 99885740')
busca = nova_agenda.buscar('Helldanio')
print(busca)
nova_agenda.listar()
nova_agenda.remover('Luzinete')
nova_agenda.listar()

#exercício 08
class Cliente:

    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

    def imprime(self):
        print('Nome:',self.nome)
        print()
        print('Idade:',self.idade)
        print()
        print('E-mail:',self.email)

novo_cliente = Cliente('Helldanio',48,'helldanio@gmail.com')
novo_cliente.imprime()
'''
#exercício 09
class Cliente:

    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

    def incluir(self, nome, idade, email):
        inclui = True
        if len(dados) > 0:
            for x in dados:
                if nome == x[0]:
                    inclui = False
        if inclui:
            dados.append([nome,idade,email])
        else:
            print('Cadastro já efetivado!')

    def buscar(self, nome):
        for x in dados:
            if nome == x[0]:
                return(x)
        return([])

    def alterar(self, cliente, nome, idade, email):
        for x in range(len(dados)):
            if dados[x] == cliente:
                dados[x] = [nome, idade, email]


def cad_cli():
    nome = input('Informe o nome: ')
    idade = int(input('Infore a idade: '))
    email = input('Informe o e-mail: ')
    cadastro.incluir(nome,idade,email)

def alt_cli():
    nome = input('Informe o nome para alteração: ')
    cli = cadastro.buscar(nome)
    if len(cli) > 0:
        novo_nome = input('Informe o novo nome: ')
        nova_idade = int(input('Informe a nova idade: '))
        novo_email = input('Informe o novo e-mail: ')
        cadastro.alterar(cli,novo_nome,nova_idade,novo_email)
    else:
        print('Cliente não encontrado!')

dados = []
opcao = 0
cadastro = Cliente()
while opcao != 3:
    print('------------------------------------')
    print('  SISTEMA DE CADASTRO DE CLIENTES')
    print('------------------------------------')
    print('1. Cadastrar novo cliente')
    print('2. Alterar cliente')
    print('3. Sair')
    print()
    opcao = input('Escolha sua opção: ')
    if not opcao.isdigit():
        print('Opção inválida!')
        opcao = 0
    else:
        opcao = int(opcao)
        if opcao == 1:
            cad_cli()
        elif opcao == 2:
            alt_cli()
        elif opcao == 3:
            print('Sistema finalizado!')
        else:
            print('Opção inválida!')

#exercício 10
class ContaCorrente:
    
    def __init__(self, cliente, saldo):
        self.cliente = cliente
        self.saldo = saldo

    def deposito(self, valor):
        self.saldo += valor
        print(f'Saldo atual: {self.saldo:.2f}')

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print('Saldo insuficiente!')
        print(f'Saldo atual: {self.saldo:.2f}')

    def transferencia(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print('Saldo insuficiente!')
        print(f'Saldo atual: {self.saldo:.2f}')
    
dados = []
novo_cliente = Cliente('Helldanio',48,'helldanio@gmail.com')
conta_corrente = ContaCorrente(novo_cliente,5000)
conta_corrente.saque(2000)
conta_corrente.transferencia(3100)
conta_corrente.transferencia(3000)
'''
#exercício 11
class Fracao:

    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __add__(self, fracao):
        if self.denominador == fracao.denominador:
            n = self.numerador + fracao.numerador
            d = self.denominador
        else:
            n = self.numerador*fracao.denominador+self.denominador*fracao.numerador
            d = self.denominador*fracao.denominador
        return(Fracao(n,d))

    def __sub__(self, fracao):
        if self.denominador == fracao.denominador:
            n = self.numerador - fracao.numerador
            d = self.denominador
        else:
            n = self.numerador*fracao.denominador-self.denominador*fracao.numerador
            d = self.denominador*fracao.denominador
        return(Fracao(n,d))

    def __mul__(self, fracao):
        n = self.numerador * fracao.numerador
        d = self.denominador * fracao.denominador
        return(Fracao(n,d))

    def __truediv__(self, fracao):
        n = self.numerador * fracao.denominador
        d = self.denominador * fracao.numerador
        return(Fracao(n,d))

    def __lt__(self, fracao):
        return(self.numerador/self.denominador < fracao.numerador/fracao.denominador)

    def __le__(self, fracao):
        return(self.numerador/self.denominador <= fracao.numerador/fracao.denominador)

    def __eq__(self, fracao):
        return(self.numerador/self.denominador == fracao.numerador/fracao.denominador)

    def __ne__(self, fracao):
        return(self.numerador/self.denominador != fracao.numerador/fracao.denominador)

    def __gt__(self, fracao):
        return(self.numerador/self.denominador > fracao.numerador/fracao.denominador)

    def __ge__(self, fracao):
        return(self.numerador/self.denominador >= fracao.numerador/fracao.denominador)

    def __repr__(self):
        return(f'A Fração é {str(self.numerador)}/{str(self.denominador)}')


f1 = Fracao(5,2)
f2 = Fracao(7,5)
a = f1 + f2
print(a)
b = f1 - f2
print(b)
c = f1 * f2
print(c)
d = f1 / f2
print(d)
print(f1<f2)
print(f1<=f2)
print(f1==f2)
print(f1!=f2)
print(f1>f2)
print(f1>=f2)

#exercício 12
from datetime import date, datetime

class Data:

    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.data = datetime(self.ano,self.mes,self.dia)

    def __lt__(self, data):
        return(self.data < data.data)

    def __le__(self, data):
        return(self.data <= data.data)

    def __eq__(self, data):
        return(self.data == data.data)

    def __ne__(self, data):
        return(self.data != data.data)

    def __gt__(self, data):
        return(self.data > data.data)

    def __ge__(self, data):
        return(self.data >= data.data)

    def __repr__(self):
        return(f'A Data é {self.data.strftime("%d/%m/%Y")}')

data1 = Data(25,2,2022)
data2 = Data(10,3,2022)
print(data1>data2)
print(data1)

#exercício 13 - Resolvido com a implementação do método __repr__ nos exercício 1,2,3,4 e 6

#exercício 14
class Quadrado(Retangulo):

    def __init__(self, lado_a):
        super().__init__(lado_a, lado_a)

    def area(self):
        return(self.lado_a**2)

    def __repr__(self):
        return(f'Os lados do quadrado tem tamanho de {self.lado_a} cm')

qua1 = Quadrado(6)
print(qua1)
print(f'A área do quadrado é de {qua1.area()} cm2')
'''
# exercício 15
class ContaVip(ContaCorrente):

    def __init__(self, cliente, saldo, cheque_especial):
        super().__init__(cliente, saldo+cheque_especial)
        