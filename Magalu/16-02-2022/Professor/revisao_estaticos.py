# Objetivo:
# Poder criar usuários (classe Usuario)
# Poder armazenar uma coleção de usuários (classe BancoDeUsuarios)

# Imprimir tabela de usuarios:
#      Paulo | paulo@email.com
#    Matheus | matheus@email.com
# ...
class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class BancoDeUsuarios:
    espacamento_de_exibicao = 1 # Atributo estático

    def __init__(self, lista_de_usuarios=[]):
        self.lista_de_usuarios = lista_de_usuarios

    def exibir(self):
        print('---------------------------------')

        n = BancoDeUsuarios.espacamento_de_exibicao

        for usuario in self.lista_de_usuarios:
            print(f"{usuario.nome:>10s}{' '*n}|{' '*n}{usuario.email:<20s}")

        print('---------------------------------')

    # Método estático
    @staticmethod
    def alterar_espacamento(novo_espacamento):
        BancoDeUsuarios.espacamento_de_exibicao = novo_espacamento

banco1 = BancoDeUsuarios([
    Usuario('Paulo', 'paulo@email.com'),
    Usuario('Matheus', 'matheus@email.com'),
    Usuario('Angelita', 'angelita@email.com')
])

banco2 = BancoDeUsuarios([
    Usuario('Amanda', 'amanda@email.com'),
    Usuario('Rodrigo', 'rodrigo@email.com')
])

banco1.exibir()
banco2.exibir()

BancoDeUsuarios.alterar_espacamento(3)

banco1.exibir()
banco2.exibir()
