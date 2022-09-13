import random
alu1 = str(input('Digite o primeiro aluno: '))
alu2 = str(input('Digite o segundo aluno: '))
alu3 = str(input('Digite o teceiro aluno: '))
chose = random.choice([alu1, alu2, alu3])
print ('O escolhido foi {}'.format(chose))

