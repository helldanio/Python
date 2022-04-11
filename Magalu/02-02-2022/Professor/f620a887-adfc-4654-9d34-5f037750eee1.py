class Retângulo:

    def __init__(self, lado_a, lado_b):

        self.lado_a = lado_a
        self.lado_b = lado_b

    def area(self):

        return self.lado_a*self.lado_b

ret1 = Retângulo(2,6)

print(ret1.lado_a)
print(ret1.lado_b)
print(f' A área do retângulo 1 é {ret1.area()} cm^2')

# Classe: é algo abrangente no sentido de reunir de maneira geral um grupo

# Objeto: Ele depende da classe e possuí atributos particulares

# Atributo: característica de uma classe que pode ser passada aos objetos

# Método: são as ações dentro de uma classe e dependem dos atributos
