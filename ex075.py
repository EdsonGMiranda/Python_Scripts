# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final,
# mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.


i = 0
valores = []
while i < 4:
    valor = int(input(f'Entre com o {i+1}º número:'))
    valores.append(valor)
    i += 1

print('-=' * 10)
print(f'O número 9 foi digitado {valores.count(9)} vezes.')
print('-=' * 10)
if valores.count(3) == 0:
    print('Não foi digitado nenhum valor = 3.')
else:
    print(f'O primeiro valor 3 encontrado está na  {valores.index(3)+1} posição.')
print('-=' * 10)
print('Os valores pares são:')
print('-=' * 10)
for count in valores:
    if count % 2 == 0:
        print(f'{count}', end=' ')
print(' ')
print('-=' * 10)
