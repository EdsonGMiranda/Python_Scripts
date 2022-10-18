# Exercício Python 7: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input('Digite a nota do primeiro semestre : '))
n2 = float(input('Digite a nota do segundo semestre : '))
m = (n1 + n2) /2
print('A média entre {} e {} é igual a {}' .format(n1, n2, m))
