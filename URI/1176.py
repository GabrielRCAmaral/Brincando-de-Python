# -*- coding: utf-8 -*-
def add(lista,i):
    lista.append(lista[i-1]+lista[i-2])

n=int(input())
lista=[0,1]
for i in range(2,61):
    add(lista,i)
for i in range(n):
    a=int(input())
    print 'Fib(%i) = %i'%(a,int(lista[a]))