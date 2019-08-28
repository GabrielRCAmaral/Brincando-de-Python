# -*- coding: utf-8 -*-
import math
a,b,c= raw_input().split(" ")
a=float(a)
b=float(b)
c=float(c)

if pow(b,2)-4*a*c <0 or a==0:
    print "Impossivel calcular"
else:
    delta=pow(b,2)-4*a*c
    r1=(-b+math.sqrt(delta))/(2*a)
    r2=(-b-math.sqrt(delta))/(2*a)
    print "R1 = %.5f" %r1
    print "R2 = %.5f" %r2   
