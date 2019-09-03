# -*- coding: utf-8 -*-
ent=raw_input().split()
dados=[int(ent[0]),int(ent[1])]
while(dados[0]!=0 and dados[1]!=0):
    if dados[0]>0 and dados[1]>0:
        print 'primeiro'
    elif dados[0]>0 and dados[1]<0:
        print 'quarto'
    elif dados[0]<0 and dados[1]<0:
        print 'terceiro'
    else:
        print 'segundo'
    ent=raw_input().split()
    dados=[int(ent[0]),int(ent[1])]