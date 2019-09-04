# -*- coding: utf-8 -*-

def ganhou(lista):
    lis=[int(lista[0]),int(lista[1])]
    if lis[0]<lis[1]:
        return 'grem'
    if lis[0]>lis[1]:
        return 'inter'
    return 'emp'
total=0
gre=0
inter=0
emp=0
cont=1
while (cont!=2):
    n=raw_input().split()
    ganhador=ganhou(n)
    if ganhador=='grem':
        gre+=1
    elif ganhador=='inter':
        inter+=1
    else:
        emp+=1
    total+=1
    print 'Novo grenal (1-sim 2-nao)'
    cont=int(input())
print '%i grenais' %total
print 'Inter:%i'%inter
print 'Gremio:%i'%gre
print 'Empates:%i'%emp
if gre>inter:
    print 'Gremio venceu mais'
else:
    print 'Inter venceu mais'


