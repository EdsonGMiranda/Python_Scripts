# Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de
# um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(larg, comp):
    a = larg * comp
    print(f'A area de um terreno é de {larg} x {comp} é de {a}m²')


print(f'---CONTROLE DE TERRENOS---')
l = float(input('Entre com a Largura(m): '))
c = float(input('Entre com o Comprimento(m): '))
print('-*' * 20)
area(l, c)
