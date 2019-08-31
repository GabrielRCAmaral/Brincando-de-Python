# -*- coding: utf-8 -*-
numeros=[]
for i in range(5):
    numeros.append(int(input()))
pares=0
impares=0
positivo=0
negativo=0
for valor in numeros:
    if valor>=0:
        positivo+=1
    else:
        negativo+=1
    if valor%2==0:
        pares+=1
    else:
        impares+=1
print "%i valor(es) par(es)" %pares
print "%i valor(es) impar(es)" %impares
print "%i valor(es) positivo(s)" %positivo
print "%i valor(es) negativo(s)" %negativo


