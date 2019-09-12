# -*- coding: utf-8 -*-
n=int(input())
op=raw_input()
matriz=[]
for i in range(12):
    linha=[]
    for y in range(12):
        linha.append(float(input()))
    matriz.append(linha)

soma=0
for i in range(12):
    soma+=matriz[i][n]
print '%.1f'%(soma if(op is 'S')  else soma/12)
