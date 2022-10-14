# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
i = 0
lista = []
maior = menor = 0
for i in range(0, 5):
    lista.append(int(input(f'Entre com o {i+1}º valor: ')))

    if lista[i] > maior:
        maior = lista[i]

    else:
        menor = lista[i]

print(f'A lista que você digitou foi {lista}')
print(f'O maior valor da lista é {maior} e a posição é ', end=' ')
for pos, j in enumerate(lista):
    if j == maior:
        print(f'{pos}', end=' ')

print(f'\nO menor valor da lista é {menor} e a posição é ', end=' ')
for pos, j in enumerate(lista):
    if j == menor:
        print(f'{pos}', end=' ')
