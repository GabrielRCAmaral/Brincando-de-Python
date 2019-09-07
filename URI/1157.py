# -*- coding: utf-8 -*-
n=int(input())
lista=[x for x in range(1,n+1) if n%x==0]
for i in lista:
    print i