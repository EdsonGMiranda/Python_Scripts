# Exercício Python 089:Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar
# as notas de cada aluno individualmente.
from time import sleep
media = n = 0
nota = list()
aluno = list()
aluno_nota = list()
# tudo = [[' ', [0, 0]], [' ', [0, 0]]]
while True:
    nome = input('Entre com o nome: ')
    soma = 0
    for i in range(0, 2):
        prova = float(input('Entre com a nota: '))
        nota.append(prova)
        soma += nota[i]
    aluno.append(nome)
    aluno.append(nota[:])
    aluno.append(soma/2)
    aluno_nota.append(aluno[:])
    nota.clear()
    aluno.clear()

    sair = input('Deseja sair? [S/N]').upper().split()[0]
    if sair in 'N':
        break

print('-*-' * 15)
print(f'{"No.":<4} {"NOME":<10} {"Média":<8}')
for p, l in enumerate(aluno_nota):
    print(f'{p:<4} {l[0]:<10} {l[2]:<8}')
print('-*-' * 15)

while n != 999:
    esc = int(input('Mostrar notas de qual aluno: (999 para sair): '))
    if esc == 999:
        print('FINALIZANDO...', end='')
        sleep(1)
        print('...', end='')
        sleep(1)
        print('...')
        break
    elif esc <= len(aluno_nota) - 1:
        for p, l in enumerate(aluno_nota):
            if p == esc:
                print(f'Notas de {l[0]} são {l[1]}')




