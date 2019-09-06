# -*- coding: utf-8 -*-
lin=raw_input().split()
lista=map(int,lin)
valores=[x+lista[0] for x in range(lista[-1])]
soma=0
for i in valores:
    soma+=i
print soma