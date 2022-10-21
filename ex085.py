# Exercício Python 085: crie um programa onde o usuário possa digitar sete valores numéricos e
# cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final,
# mostre os valores pares e ímpares em ordem crescente.

lista = [[], []]
valor = 0

for i in range(0, 7):
    valor = int(input(f'Entre com o {i+1}ª valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)

#print(lista)
lista[0].sort()
lista[1].sort()
print('Valores pares', end=' ')
print(f'{lista[0]}')
print('Valores impares', end=' ')
print(f'{lista[1]}')
