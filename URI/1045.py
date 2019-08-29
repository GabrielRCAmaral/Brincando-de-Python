# -*- coding: utf-8 -*-
x=raw_input().split()
x=map(float,x)
x.sort(reverse=True)
if x[0]>=x[1]+x[2]:
    print "NAO FORMA TRIANGULO"
else:
    if x[0]**2==x[1]**2+x[2]**2:
        print "TRIANGULO RETANGULO"
    if x[0]**2<x[1]**2+x[2]**2:
        print "TRIANGULO ACUTANGULO"
    if x[0]**2>x[1]**2+x[2]**2:
        print "TRIANGULO OBTUSANGULO"
    if x[0]==x[1]==x[2]:
        print "TRIANGULO EQUILATERO"
    elif x[0]==x[1] or x[1]==x[2] or x[2]==x[0]:
        print "TRIANGULO ISOSCELES"
