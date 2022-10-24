# Exercício Python 090: Faça um programa que leia nome e média de um aluno,
# guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

aluno = {}

nome = str(input('Nome: '))
media = float(input('Média: '))
if media >= 7:
    situacao = 'Aprovado'
elif 5 <= media < 7:
    situacao = 'Recuperação'
else:
    situacao = 'Reprovado'
aluno['Nome'] = nome
aluno['Media'] = media
aluno['Situacao'] = situacao

for k, v in aluno.items():
    print(f'O {k} do aluno é {v}')



print(aluno)