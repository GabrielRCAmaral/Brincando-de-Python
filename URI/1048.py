# -*- coding: utf-8 -*-
salario=float(input())
if salario<=400:
    novo=salario*1.15
    re=0.15*salario
    per=15
elif salario<=800:
    novo=salario*1.12
    re=0.12*salario
    per=12
elif salario<=1200:
    novo=salario*1.10
    re=0.1*salario
    per=10
elif salario<=2000:
    novo=salario*1.07
    re=0.07*salario
    per=7
else:
    novo=salario*1.04
    re=0.04*salario
    per=4
print "Novo salario:",novo
print "Reajuste ganho:",re
print "Em percentual: %i %%" %per

