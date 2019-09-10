# -*- coding: utf-8 -*-
def veri(num):
    soma=0
    lista=[x for x in range(1,num) if not num%x]
    print lista
    for i in lista:
        soma+=i
    return '%i eh perfeito'%num if (soma==num) else '%i nao eh perfeito'%num
n=int(input())
for i in range(n):
    num=int(input())
    print veri(num)
    