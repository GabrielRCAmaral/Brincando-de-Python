# -*- coding: utf-8 -*-

def add(lista,i):
    lista.append(lista[i]/2)

n=float(input())
lista=[n]
for i in range(99):
    add(lista,i)
for i,item in enumerate(lista):
    print 'N[%i] = %.4f'%(i,item)