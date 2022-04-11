turma = {'Código':839, 'Linguagem':'Python', 'Matriculados':25, 
'Empresa':'Magazine Luiza', 'Professores':['Rafael', 'Matheus']}

print(turma['Linguagem'])
print(turma['Empresa'])


turma['Módulo'] = 1

print(turma)

for chave in turma:
    print(chave, '-', turma[chave])

if 'Empresa' in turma:
    print('A nossa empresa é:', turma['Empresa'])
else:
    turma['Empresa'] = 'Novíssima Empresa S/A'

print(turma)

# lista de todas as chaves:
chaves = list(turma.keys())
print(chaves)
valores = list(turma.values())
print(valores)

for professor in turma['Professores']:
    print('Prof.', professor)
