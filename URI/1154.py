# -*- coding: utf-8 -*-

def soma(lista):
    soma=0
    for i in lista:
        soma+=i
    return soma
lista=[]
n=0
while(n>=0):
    n=int(input())
    if(n>=0):
        lista.append(n)
else:
    print '%.2f'%(soma(lista)/float(len(lista)))