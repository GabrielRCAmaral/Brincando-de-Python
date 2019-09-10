# -*- coding: utf-8 -*-
def calcAno(lista):
    a=int(lista[0])
    b=int(lista[1])
    ga=float(lista[2])
    gb=float(lista[3])
    i=0
    while(i<=100 and a<=b):
        a+=int(a*(ga/100))
        b+=int(b*(gb/100))
        i+=1
    return '%i anos.'%i if(i<=100) else 'Mais de 1 seculo.'

n=int(input())
for i in range(n):
    print calcAno(raw_input().split())
    
    