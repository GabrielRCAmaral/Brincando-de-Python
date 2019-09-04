# -*- coding: utf-8 -*-
r=1
while(r!=2):
    if(r==1):
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
            if i==2:
                break
        
        print 'media = %.2f' %(soma/i)
        print 'novo calculo (1-sim 2-nao)'
    else:
        print 'novo calculo (1-sim 2-nao)'
    r=int(input())
