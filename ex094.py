# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista
# com as mulheres D) Uma lista de pessoas com idade acima da média
pessoas = dict()
lista = list()
list_fem = list()
list_adm = list()
media = soma = 0
while True:
    pessoas["nome"] = str(input('Nome: '))
    while True:
        pessoas["sexo"] = str(input('Sexo: [F/M] ')).upper().strip()[0]
        if pessoas["sexo"] in 'MF':
            break
    pessoas["idade"] = int(input('Idade: '))
    soma += pessoas["idade"]
    lista.append(pessoas.copy())
    if pessoas["sexo"] == 'F':
        list_fem.append(pessoas.copy())
    sair = input('Deseja continuar? [S/N]').upper().strip()[0]
    if sair in 'N':
        break
print('-*-' * 15)
print(f'Foram cadastradas {len(lista)} pessoas')
print('-*-' * 15)

media = soma / len(lista)
print(f' A média de idade é {media}.')

for p, i in enumerate(lista):
    if lista[p]["idade"] > media:
        list_adm.append(lista[p])

print('-*-' * 15)
print(f'Lista de mulheres cadastradas {list_fem}')
print('-*-' * 15)
print(f'Lista de pessoas mais velhas que a média {list_adm}')
print('-*-' * 15)

