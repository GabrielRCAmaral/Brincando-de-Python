# -*- coding: utf-8 -*-
x1=raw_input()
d1=str(x1[4:])
x2=raw_input().split(" : ")
y1=raw_input()
d2=str(y1[4:])
y2=raw_input().split(" : ")

ht1=int(x2[2])+int(x2[1])*60+int(x2[0])*60*60+int(d1)*24*60*60
ht2=int(y2[2])+int(y2[1])*60+int(y2[0])*60*60+int(d2)*24*60*60
data=ht2-ht1
print "%i dia(s)" %(data/60/60/24)
print "%i hora(s)" %(data/60/60%24)
print "%i minuto(s)" %(data%60)
print "%i segundo(s)" %(data%60)
