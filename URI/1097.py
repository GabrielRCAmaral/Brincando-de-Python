# -*- coding: utf-8 -*-
I=0
j=1
for i in range(5):
    for k in range(3):
        print "I=%i J=%i" %(I,j)
        j-=1
    I+=2
    j+=5