# -*- coding: utf-8 -*-
x=float(input())

if(x<=2000):
    print "Isento"
elif(x<=3000):
    print "R$ %.2f" %((x-2000)*0.08)
elif (x<=4500):
    print "R$ %.2f" %((x-3000)*0.18+1000*0.08)
else:
    print "R$ %.2f" %((x-4500)*0.28+1500*0.18+1000*0.08)
    
