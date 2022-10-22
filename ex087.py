# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.


matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = soma3 = mai = 0


for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l, c}]: '))

print('-*' * 15)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^6}]', end='')
    print()


for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]

print('-*' * 15)
print(f'A Soma dos numeros pares da matriz é {soma}')

for l in range(0, 3):
    soma3 += matriz[l][2]


print()
print('-*' * 15)
print(f'A Soma dos valores da terceira coluna é {soma3}')


for l in range(0, 3):
    for c in range(0, 3):
        mai = matriz[1][c]
        if matriz[1][c] > mai:
            mai = matriz[1][c]
print()
print('-*' * 15)
print(f'O maior valor da segunda coluna é {mai}')



