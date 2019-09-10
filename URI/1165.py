# -*- coding: utf-8 -*-
def veri(num):
    lista=[x for x in range(1,num) if not num%x]
    return '%i eh primo'%num if (len(lista)==1) else '%i nao eh primo'%num
n=int(input())
for i in range(n):
    num=int(input())
    print veri(num)
    