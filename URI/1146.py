# -*- coding: utf-8 -*-
n=int(input())
while(n):
    lista=[x for x in range(1,n+1)]
    print str(lista).replace('[','').replace(',','').replace(']','')
    n=int(input())