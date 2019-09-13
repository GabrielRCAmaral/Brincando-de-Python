# -*- coding: utf-8 -*-
op=raw_input()
matriz=[]
for i in range(12):
    linha=[]
    for y in range(12):
        linha.append(float(input()))
    matriz.append(linha)

soma=0
n=0
for i in range(12):
    for y in range(12):
        if y<len(matriz[i])-1-i:
            soma+=matriz[i][y]
            n+=1
print '%.1f'%(soma if(op is 'S')  else soma/n)
