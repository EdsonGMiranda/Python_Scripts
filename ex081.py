# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

list_num = []
count = 0
while True:
    list_num.append(int(input('Entre com um valor: ')))
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Desaja continuar? [S/N]')).upper().strip()[0]
    if sair == 'N':
        break


print('-=-' * 20)
print(f'Foram digitados {len(list_num)} valores.')
list_num.sort(reverse=True)
print(f'A lista ordenada de forma decrescente é {list_num}')

if 5 in list_num:
    print('O valor 5 foi digitado.')
else:
    print('O valor 5 não foi digitado.')

