# -*- coding: utf-8 -*-
lista=[]
for i in range(20):
    lista.append(float(input()))
lista.reverse()
for i,item in enumerate(lista):
    print 'N[%i] = %i'%(i,item)
    
