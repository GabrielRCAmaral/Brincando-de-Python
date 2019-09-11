# -*- coding: utf-8 -*-

def add(lista,i):
    lista.append(lista[i]*2)

n=int(input())
lista=[n]
for i in range(9):
    add(lista,i)
for i,item in enumerate(lista):
    print 'N[%i] = %i'%(i,item)