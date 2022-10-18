# Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

d = float(input('Digite uma distancia :'))
km = d / 1000
hm = d / 100
dam = d / 10
dm = d * 10
cm = d * 100
mm = d * 1000

print('A medida de {}m corresponde há \n {}km\n {}hm\n {}dam\n {}dm \n {}cm  \n {}mm' .format(d, km, hm, dam, dm, cm, mm))

