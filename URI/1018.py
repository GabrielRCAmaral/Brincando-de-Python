# -*- coding: utf-8 -*-
valor=int(input())
valorIn=valor
n100=valor//100
valor=valor%100
n50=valor//50
valor=valor%50
n20=valor//20
valor=valor%20
n10=valor//10
valor=valor%10
n5=valor//5
valor=valor%5
n2=valor//2
valor=valor%2
print valorIn
print n100,"nota(s) de R$ 100,00"
print n50,"nota(s) de R$ 50,00"
print n20,"nota(s) de R$ 20,00"
print n10,"nota(s) de R$ 10,00"
print n5,"nota(s) de R$ 5,00"
print n2,"nota(s) de R$ 2,00"
print valor,"nota(s) de R$ 1,00"