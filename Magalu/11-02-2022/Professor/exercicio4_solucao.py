# 4. Classe Conta Corrente: Crie uma classe para implementar uma conta corrente
#     - Atributos: número da conta, nome do correntista e saldo
#     - Métodos: alterar_nome, deposito e saque; No construtor, saldo é opcional,
#       com valor default zero e os demais atributos são obrigatórios.

class ContaCorrente:

    def __init__(self, numero, nome_do_correntista, saldo=0):
        self.numero = numero
        self.nome_do_correntista = nome_do_correntista
        self.saldo = saldo

    def mostrar_informacoes(self):
        print(f'Correntista: {self.nome_do_correntista} | Numero: {self.numero} | Saldo: {self.saldo}')

    def alterar_nome(self, novo_nome):
        self.nome_do_correntista = novo_nome

    def fazer_deposito(self, quantia):
        if quantia >= 0:
            self.saldo += quantia

    # def pedir_e_alterar_nome(self):
    #     novo_nome = input("Digite o novo nome: ")
    #     self.nome_do_correntista = novo_nome

    def fazer_saque(self, quantia):
        # Primeiro calculamos o novo saldo (note que não tem
        # o self, pois é apenas pra uso dentro do método)
        novo_saldo = self.saldo - quantia

        # Para poder sacar o valor da conta, esse
        # valor precisa ser positivo.
        # Também é necessário que o valor a ser sacado
        # seja maior ou igual ao que tem na conta,
        # pois não podemos, por exemplo, tirar
        # 500 reais de uma conta com 300.
        # Por isso o novo_saldo deve ser maior
        # ou igual a 0
        if quantia >= 0 and novo_saldo >= 0:
            self.saldo = novo_saldo

        # Note que, se as condições não
        # forem satisfeitas, a operação
        # simplesmente não será feita.

conta_do_paulo = ContaCorrente(123, 'Paulo')
conta_do_paulo.mostrar_informacoes()

conta_do_paulo.fazer_deposito(300)
conta_do_paulo.mostrar_informacoes()

conta_do_paulo.fazer_saque(200)
conta_do_paulo.mostrar_informacoes()

    



