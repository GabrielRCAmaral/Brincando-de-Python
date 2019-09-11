# -*- coding: utf-8 -*-

n=int(input())
y=0
lista=[]
for i in range(1000):
    if y<n:
        lista.append(y)
        y+=1
    else:
        y=0
        lista.append(y)
        y+=1

    
for i,item in enumerate(lista):
    print 'N[%i] = %i'%(i,item)