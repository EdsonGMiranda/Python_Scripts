n1 = float(input('Entre com o primeiro numero: '))
menor = n1
maior = n1
n2 = float(input('Entre com o segundo numero: '))
if n2 > maior:
    maior = n2
    menor = n1
else:
    maior = n1
    menor = n2
n3 = float(input('Entre com o terceiro numero: '))
if n3 > maior:
    maior = n3
if n3 < menor:
    menor = n3

print('O maior numero é {}'.format(maior))
print('O menor numero é {}'.format(menor))


