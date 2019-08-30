# -*- coding: utf-8 -*-
lista=[]
for i in range(0,6):
   lista.append(int(input()))
cont=0
for i in lista:
    if i>=0:
        cont+=1
print "%i valores positivos" %cont