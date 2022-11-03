# Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora
# a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.


def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print(f'\033[31mERRO! Digite um numero inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print(f'\033[31mERRO! Digite um número flutuante válido.\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0.0
        else:
            return n


num = leiafloat('Digite um numero: ')
print(f'Você acabou de digitar o número {num}')

num = leiaint('Digite um numero: ')
print(f'Você acabou de digitar o número {num}')
