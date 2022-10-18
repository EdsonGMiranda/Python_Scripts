# Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input('Qual o salario do funcionario ? '))
if sal > 1250:
    n_sal = sal + sal * 0.10
else:
    n_sal = sal + sal * 0.15
print('Quem ganhava R${:.2f} passa a ganhar o salario de R${:.2f} '.format(sal, n_sal))
