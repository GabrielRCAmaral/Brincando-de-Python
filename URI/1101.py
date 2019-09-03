# -*- coding: utf-8 -*-
ent=raw_input().split()
dados=[int(ent[0]),int(ent[1])]
while(dados[0]>0 and dados[1]>0):
    dados.sort()
    sum=0
    saida=""
    for i in range(dados[0],dados[1]+1):
        saida+=str(i)+' '
        sum+=i
    saida+='Sum=%i'%sum
    print saida
    ent=raw_input().split()
    dados=[int(ent[0]),int(ent[1])]