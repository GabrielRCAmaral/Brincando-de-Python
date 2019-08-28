# -*- coding: utf-8 -*-
valor=float(input())

valorInt=int(valor)
valorFloat=valor-valorInt
valorFloat*=100

n100=valorInt//100
valorInt=valorInt%100
n50=valorInt//50
valorInt=valorInt%50
n20=valorInt//20
valorInt=valorInt%20
n10=valorInt//10
valorInt=valorInt%10
n5=valorInt//5
valorInt=valorInt%5
n2=valorInt//2
valorInt=valorInt%2

m50=valorFloat//50
valorFloat%=50
m25=valorFloat//25
valorFloat%=25
m10=valorFloat//10
valorFloat%=10
m5=valorFloat//5
valorFloat%=5

print 'NOTAS:'
print n100,"nota(s) de R$ 100,00"
print n50,"nota(s) de R$ 50,00"
print n20,"nota(s) de R$ 20,00"
print n10,"nota(s) de R$ 10,00"
print n5,"nota(s) de R$ 5,00"
print n2,"nota(s) de R$ 2,00"

print 'MOEDAS:'
print valorInt,"moeda(s) de R$ 1,00"
print int(m50),"moeda(s) de R$ 0,50"
print int(m25),"moeda(s) de R$ 0,25"
print int(m10),"moeda(s) de R$ 0,10"
print int(m5),"moeda(s) de R$ 0,05"
print int(valorFloat),"moeda(s) de R$ 0,01"
