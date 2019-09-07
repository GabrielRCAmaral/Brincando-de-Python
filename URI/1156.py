# -*- coding: utf-8 -*-
soma=0.00
for i in range(1,20):
    soma+=float(2*i+1)/(2**i)
    print (2*i)
print '%.2f'%(soma+1)