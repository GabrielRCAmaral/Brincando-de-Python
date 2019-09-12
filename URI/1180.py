# -*- coding: utf-8 -*-
n=int(input())
lista=map(int,raw_input().split())
print 'Menor valor: %i'%min(lista)
print 'Posicao: %i'%(lista.index(min(lista)))