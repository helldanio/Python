# Informe a média de 2 notas e diga se o aluno está aprovado.
# - se o aluno tirar pelo menos 6, está aprovado
# - se o aluno tirar entre 3 e 6, ele fará exame
# - se o aluno tirar menos do que 3, ele está reprovado
# Considere também a presença: 
# - De um total de 12 aulas, o aluno deve vir em mais do que 9

n1 = float(input('Digite a sua nota 1: '))
n2 = float(input('Digite a sua nota 2: '))
presenca = int(input('Digite a presença: '))

media = (n1 + n2) / 2

if media >= 6 and presenca > 9: 
    print('Aprovado')
elif media >= 3:
    print('Exame')
else:
    print('Reprovado')

'''
if media >= 6: 
    print('Aprovado')
else:
    if media >= 3:
        print('Exame')
    else:
        print('Reprovado')
'''
print(media)


'''
Operadores lógicos
> maior que
< menor que
>= maior ou igual
<= menor ou igual
!= diferente
== igual
'''