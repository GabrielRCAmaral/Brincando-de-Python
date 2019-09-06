# -*- coding: utf-8 -*-
x=int(input())
y=int(input())
soma=0
while(y<=x):
    y=int(input())
i=0
while(soma<y):
    soma+=x
    x+=1
    i+=1
print i
