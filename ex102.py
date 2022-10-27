# Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que
# indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou
# não na tela o processo de cálculo do fatorial.

def fatorial(n, show=False):
    """
    => Calculando Fatórial
    :param n: O número a ser calculado.
    :param show: (opcional) se mostra ou não a conta.
    :return: o valor fatorial de n.
    """
    fat = n
    soma = 1
    print(f'Calculando {n}!= ', end='')
    if show == True:
        while fat > 0:
            print(f'{fat}', end='')
            print(' x ' if fat > 1 else ' = ', end='')
            soma *= fat
            fat -= 1
        return soma
    else:
        while fat > 0:
            soma *= fat
            fat -= 1
        return soma


print(fatorial(4, show=True))
print()
print(fatorial(3, show=False))
print()
print(fatorial(5))
print()
print(fatorial(7,True))
