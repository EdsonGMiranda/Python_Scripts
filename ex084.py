# Exercício Python 084: faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.


pessoas = list()
dados = list()
maior = menor = 0
while True:
    dados.append(input('Entre com o Nome: '))
    dados.append(int(input('Entre com o Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()

    sair = ' '
    if sair not in 'SN':
        sair = input('Deseja continuar? [S/N]').upper().split()[0]
        if sair == 'N':
            break

print('-*' * 20)
print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'O maior peso foi de {maior}kg, Peso de ', end=' ')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]')
print(f'O menor peso foi de {menor}kg, Peso de', end=' ')
for i in pessoas:
    if i[1] == menor:
        print(f'[{i[0]}]')

