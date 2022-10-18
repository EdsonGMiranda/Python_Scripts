# Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random
alu1 = str(input('Digite o primeiro aluno: '))
alu2 = str(input('Digite o segundo aluno: '))
alu3 = str(input('Digite o teceiro aluno: '))
chose = random.choice([alu1, alu2, alu3])
print ('O escolhido foi {}'.format(chose))

