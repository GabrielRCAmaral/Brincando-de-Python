# -*- coding: utf-8 -*-
x=raw_input().split()
x=map(int,x)
if x[0]<x[2] and x[1]<x[3] :
    print "O JOGO DUROU %i HORA(S) E %i MINUTO(S)" %(x[2]-x[0],x[3]-x[1])
elif x[0]<x[2] and x[1]>x[3] :
    print "O JOGO DUROU %i HORA(S) E %i MINUTO(S)" %(x[2]-x[0]-1,60-x[1]+x[3])
elif x[0]<x[2] and x[1]==x[3] :
    print "O JOGO DUROU %i HORA(S) E 0 MINUTO(S)" %(x[2]-x[0])
elif x[0]>x[2] and x[1]<x[3] :
     print "O JOGO DUROU %i HORA(S) E %i MINUTO(S)" %(24-x[0]+x[2],x[3]-x[1])
elif x[0]>x[2] and x[1]>x[3]:
     print "O JOGO DUROU %i HORA(S) E %i MINUTO(S)" %(24-x[0]+x[2],60-x[1]+x[3])
elif x[0]>x[2] and x[1]==x[3]:
    print "O JOGO DUROU %i HORA(S) E 0 MINUTO(S)" %(24-x[0]+x[2])
elif x[0]==x[2] and x[1]<x[3]:
    print "O JOGO DUROU 0 HORA(S) E %i MINUTO(S)" %(x[3]-x[1])
elif x[0]==x[2] and x[1]>x[3]:
    print "O JOGO DUROU 23 HORA(S) E %i MINUTO(S)" %(60-x[1]+x[3])
else:
    print "O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)"