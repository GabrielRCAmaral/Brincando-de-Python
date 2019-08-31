# -*- coding: utf-8 -*-
n=int(input())
m=int(input())
cout=0
for i in range(min(n,m)+1,max(m,n)):
    if i%2!=0:
        cout+=i
print cout 



