# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep

opc = 0
while opc != 5:
    n1 = int(input('Entre com o primeiro número: '))
    n2 = int(input('Entre com o segundo número: '))
    print('-='*15)
    opc = int(input('''
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
    >>>>>>escolha a opção: '''))
    if opc == 1:
        soma = n1 + n2
        print('A soma de {} + {} é igual  a {}'.format(n1, n2, soma))
        print('-=' * 15)
    elif opc == 2:
        multiplica = n1 * n2
        print('A multiplicação de {} x {} é igual a {}'.format(n1, n2, multiplica))
        print('-=' * 15)
    elif opc == 3:
        if n1 > n2:
           maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior é {}'.format(n1, n2, maior))
        print('-=' * 15)
    elif opc == 4:
        print('Informe os números novamente ')
        print('-=' * 15)
    elif opc == 5:
        print('Finalizando...')
        print('-=' * 15)
    else:
        print('Opção inválida!!!')
        print('-=' * 15)

print('>>>' * 5, end='')
sleep(1)
print('>>>' * 5)
sleep(1)
print('FIM DO PROGRAMA!!!')



