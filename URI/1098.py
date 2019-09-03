# -*- coding: utf-8 -*-
I=0.0
j=1.0
for i in range(11):
    if i==10:
        I=2
    for k in range(3):
        if (I==0 or I==1.0 or i==10):
            print "I=%i J=%i" %(I,j)
        else:
            print "I=%.1f J=%.1f" %(I,j)
        j+=1
    I+=0.2
    j-=2.8
   
