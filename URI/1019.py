# -*- coding: utf-8 -*-
valor=int(input())
horas=valor//60//60
minutos=valor//60%60
segundos=valor%60
print "%i:%i:%i" %(horas,minutos,segundos)