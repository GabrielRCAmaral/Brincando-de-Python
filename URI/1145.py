# -*- coding: utf-8 -*-
n,m=raw_input().split()
n=int(n)
m=int(m)
i=1
while i<=m:
    linha=''
    for y in range(n):
        linha+=str(i)+' '
        i+=1
    print linha[:-1]
    


