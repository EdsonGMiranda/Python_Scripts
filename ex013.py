# Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário,
# com 15% de aumento.

sal = float(input('Qual salario do funcionario? R$'))
aumento = 15/100
novo_sal = sal + (sal * aumento)
print('Um funcionario que ganhava R${} com um aumento de {}% agora recebe R${}'.format(sal, aumento, novo_sal))
