# -*- coding: utf-8 -*-
numeros=[]
for i in range(6):
    numeros.append(float(input()))
count=0
soma=0
for valor in numeros:
    if valor>=0:
        soma+=valor
        count+=1
print "%i valores positivos" %count
print "%.1f" %(soma/count)

