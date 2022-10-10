# Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso,
# de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

n_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
             'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
             'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
             'dezessete', 'dezoito', 'dezenove', 'vinte')

n = int(input('Digite um número entre 0 e 20: '))
i=0
while n > 22:
    n = int(input('Tente novamente, Digite um número entre 0 e 20: '))
for i in range(len(n_extenso)):
    if i == n:
        print(f'Você digitou o número {n_extenso[i]}')
        i += 1


#
#
# n_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
#              'seis', 'sete', 'oito', 'nove', 'dez','onze',
#              'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
#              'dezessete', 'dezoito',
#              'dezenove', 'vinte')
#
# while True:
#     n = int(input('Digite um número entre 0 e 20: '))
#     if 0 <= n <= 20:
#         break
#     print('Tente Novamente', end='')
# print(f'Você digitou o número {n_extenso[n]}')







