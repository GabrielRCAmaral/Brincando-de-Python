# -*- coding: utf-8 -*-
n=int(input())
for i in range(n):
    x,y=raw_input().split()
    x=int(x)
    y=int(y)
    soma=0
    p=0
    while p<y:
        if x%2!=0:
            p+=1
            soma+=x
        x+=1
    print soma

