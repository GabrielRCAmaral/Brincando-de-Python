# -*- coding: utf-8 -*-
ent=raw_input().split()
dados=[int(ent[0]),int(ent[1])]
while(dados[0]!=dados[1]):
    if dados[0]>dados[1]:
        print 'Decrescente'
    else:
        print 'Crescente'
    ent=raw_input().split()
    dados=[int(ent[0]),int(ent[1])]