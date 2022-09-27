# Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Informe seu sexo:[M/F] ')).upper().strip()[0]
while sexo not in ('M', 'F'):
    sexo = str(input('Dados inválidos, Informe seu sexo:[M/F] ')).upper().strip()[0]

print('O sexo {} foi cadastrado com sucesso!!!'.format(sexo))
