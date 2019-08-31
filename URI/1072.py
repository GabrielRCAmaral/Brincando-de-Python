# -*- coding: utf-8 -*-
n=int(input())
out=0
inn=0
for i in range(n):
    p=int(input())
    if p>=10 and p<=20:
        out+=1
    else:
        inn+=1
print "%i in" %inn
print "%i out"%out



