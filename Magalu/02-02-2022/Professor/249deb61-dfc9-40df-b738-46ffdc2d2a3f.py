'''
# POO - Programação Orientada ao Objeto


x = 1
y = 2 

def func():

    ...
    ...
    ...

    pass 

for i range(9):

    ...
    ...
    ...

# Programação Imperativa ou Procedural 

# Linguagem multiparadigma

# Haskell e o LISP

# Imperativa
# POO
# Funcional
#Programação orientada ao evento


# Progrmação Orientada ao objeto: Modularizar métodos, eventos

# Classe x Objeto: Classe   é um conjunto abrangente e os objetos fazem parte disso

# atributos: características que descrevem a classe

# método: ações da classe (funções)

'''
#Cria a classe -> Características(função - método construtor)

# Volume de uma esfera: (4/3)*pi*(r**3)
# Area de uma esfera: 4*pi*(r**2)

import math

class Esfera:

    def __init__(self,cor, raio):

        self.cor = cor
        self.raio = raio

    
    def volume(self):

        vol = (4/3)*math.pi*(self.raio**3)

        return vol

    def area(self):

        ar = 4*math.pi*(self.raio**2)

        return ar


bola1 = Esfera('vermelha', 4)
bola2 = Esfera('azul', 7)

print(f'O volume da bola 1 é {bola1.volume()} cm^3')
print(f'A area superficial da bola 1 é {bola1.area()} cm^2')


print(bola1.volume())
print(Esfera.volume(bola1))




