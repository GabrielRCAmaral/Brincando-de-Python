# -*- coding: utf-8 -*-
n=int(input())
total=0
coelhoe=0
ratos=0
sapos=0
for i in range(n):
    v=raw_input().split()
    total+=int(v[0])
    if v[1]=="C":
        coelhoe+=int(v[0])
    elif v[1]=="R":
        ratos+=int(v[0])
    else:
        sapos+=int(v[0])
print  "Total: %i cobaias" %(total)
print "Total de coelhos: %i" %coelhoe
print "Total de ratos: %i"%ratos
print "Total de sapos: %i" %sapos
print "Percentual de coelhos: %.2f %%" %((float)(coelhoe)/total*100)
print "Percentual de ratos: %.2f %%" %((float)(ratos)/total*100)
print "Percentual de sapos: %.2f %%" %((float)(sapos)/total*100)
 