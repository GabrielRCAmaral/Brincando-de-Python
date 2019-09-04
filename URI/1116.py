# -*- coding: utf-8 -*-
n=int(input())
for i in range(n):
    num=raw_input().split()
    if int(num[1])==0:
        print 'divisao impossivel'
    else:
        print '%.1f'%(float(num[0])/int(num[1]))