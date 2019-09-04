# -*- coding: utf-8 -*-
i=0
soma=0
err=0
while (err<2 or i<2):
    n=float(input())
    if (10>=n>=0):
        soma+=n
        i+=1
    else:
        err+=1
        print 'nota invalida'
   
print 'media = %.2f' %(soma/i)
print i,soma