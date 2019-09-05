# -*- coding: utf-8 -*-
a=int(input())
b=int(input())
lista=[a,b]
lista.sort()
for i in range(lista[0],lista[1]+1):
    if i%5==2 or i%5==3:
        print i
