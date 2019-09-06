# -*- coding: utf-8 -*-

x=int(input())
ant=0
prest=1
valor=0
for i in range(x):
    if i==1:
        print 1,
    else:
        print valor,
    if i:
        valor=ant+prest
        temp=prest
        prest=valor
        ant=temp
  
    