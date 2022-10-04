# Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

print('*=*' * 10)
print('LOJAS EDÃO VARIEDADES')
print('*=*' * 10)


opc = ' '
i = total = maior1000 = menor_produto = 0
n_menorproduto = ''
while True:
    print('-=-' * 10)
    print(f'Entre com o {i+1} produto : ')
    print('-=-' * 10)
    n_produto = str(input('Entre com o produto: '))
    v_preco = float(input('Entre com o preço: '))
    total += v_preco
    if v_preco > 1000:
        maior1000 += 1
    if i == 1 or v_preco < menor_produto:
        menor_produto = v_preco
        n_menorproduto = n_produto
    i += 1
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Desaja continuar? [S/N]')).upper().strip()[0]
    if sair == 'N':
        break
print('--' * 20)
print(f'O total da compra foi R${total:.2f}')
print(f'{maior1000} produtos são maiores de R$1000.00')
print(f'O produto mais barato foi {n_menorproduto} e seu valor é {menor_produto:.2f}')

