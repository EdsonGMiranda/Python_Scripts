# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma
# lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos
# digitados, em ordem crescente.


list_num = []

while True:
    n = (int(input('Entre com valor: ')))
    if n not in list_num:
        list_num.append(n)
    else:
        print('Valor já adicionado! Não vou adicionar ...')
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Desaja continuar? [S/N]')).upper().strip()[0]
    if sair == 'N':
        break

#print(list_num)
print(f'Os numeros digitados em ordem crescente são {sorted(list_num)}')





