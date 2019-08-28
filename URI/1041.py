# -*- coding: utf-8 -*-
n1,n2=raw_input().split(" ")
n1=float(n1)
n2=float(n2)
if n1>0 and n2>0:
    print "Q1"
else:
    if n2<0 and n1>0:
        print "Q4"
    else:
        if n2<0 and n1<0:
            print "Q3"
        else:
            if n2>0 and n1<0:
                print "Q2"
            else:
                if n1==0 and n2==0:
                    print "Origem"
                else:
                    if n2==0:
                        print "Eixo Y"
                    else:
                        print "Eixo X"

