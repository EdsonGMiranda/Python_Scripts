# Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços
# na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = ('Lapis', 1.75, 'Borracha', 2.00, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)

print('==' * 20)
print(f"{'LISTAGEM DE PREÇOS':^40}")
print('==' * 20)

for cont in range(0, len(produtos)):
    if cont % 2 == 0:
        print(f'{produtos[cont]:.<30} ', end='')
    else:
        print(f'R${produtos[cont]+ 1:>7.2f}')

print('==' * 20)
