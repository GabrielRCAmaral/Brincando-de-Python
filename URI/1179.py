# -*- coding: utf-8 -*-
par=[]
impar=[]
for i in range(15):
    n=int(input())
    if (not n%2):
        if(len(par)<5):
            par.append(n)
        else:
            par=[]
            par.append(n)
        for y,item in enumerate(par):
                print 'par[%i] = %i'%(y,item)
    else:
        if(len(impar)<5):
            impar.append(n)
        else:
            for y,item in enumerate(impar):
                print 'impar[%i] = %i'%(y,item)
            impar=[]
            impar.append(n)
else:

    if(len(impar)<5):
         for y,item in enumerate(impar):
            print 'impar[%i] = %i'%(y,item)

    if(len(par)<5):
         for y,item in enumerate(par):
            print 'par[%i] = %i'%(y,item)
   
