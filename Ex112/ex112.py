# Exercício Python 111: crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
# Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.

from Ex112.utilidadescev import moeda
from Ex112.utilidadescev import dado


p = dado.leiadinheiro("Digite o preço: R$")
moeda.resumo(p, 20, 30)


