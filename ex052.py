# Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo

n = int(input('Entre com um numero para saber se ele é primo: '))
for i in range(n, 1, -1):
    if n % 2 == 0 and n != 2 or n % 3 == 0 and n != 3 or n % 5 == 0 and n != 5 or  n % 7 == 0 and n != 7 or n % 11 == 0 and n != 11:
        print('O NUMERO {} NÃO É PRIMO'.format(n))
        break
    else:
        print('O NUMERO {} É PRIMO'.format(n))
        break


# num = int(input('Digite um numero: '))
# tot = 0
# for c in range(1, num +1 ):
#     if num % c == 0:
#         print('\033[33m', end='')
#         tot+=1
#     else:
#         print('\033[31m',end='')
#     print('{} '.format(c), end='')
# print('\n\033[mO numero {} foi divisivel por {} vezes '.format(num, tot))
# if tot == 2:
#     print('E por isso ele é PRIMO!')
# else:
#     print('E por isso ele NÃO É PRIMO!')
