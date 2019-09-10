# -*- coding: utf-8 -*-
n=int(input())
while(n):
    lista=[x for x in range(n,n+10) if x%2==0]
    print lista
    n=int(input())
    soma=0
    for item in lista:
        soma+=item
    print soma
