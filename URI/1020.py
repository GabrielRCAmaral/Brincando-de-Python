# -*- coding: utf-8 -*-
valor=int(input())
anos=valor//365
meses=valor%365//30
dias=valor%365%30
print "%i ano(s)" %anos
print "%i mes(s)" %meses
print "%i dia(s)" %dias