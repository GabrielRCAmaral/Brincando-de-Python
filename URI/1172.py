# -*- coding: utf-8 -*-
n=[]
for i in range(10):
    n.append(input())
for i,item in enumerate(n):
    if item<=0:
        n[i]=1
for i in range(10):
    print 'X[%i] = %i' %(i,n[i])