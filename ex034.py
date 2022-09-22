sal = float(input('Qual o salario do funcionario ? '))
if sal > 1250:
    n_sal = sal + sal * 0.10
else:
    n_sal = sal + sal * 0.15
print('Quem ganhava R${:.2f} passa a ganhar o salario de R${:.2f} '.format(sal, n_sal))
