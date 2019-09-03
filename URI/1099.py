# -*- coding: utf-8 -*-
n=int(input())
for i in range(n):
    entrada=raw_input().split()
    entrada=[int(entrada[0]),int(entrada[1])]
    entrada.sort()
    a=entrada[0]
    b=entrada[1]
    soma=0
    for y in range(a+1,b):
        if y%2!=0:soma+=y
    print soma

