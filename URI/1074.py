# -*- coding: utf-8 -*-
n=int(input())
resposta=""
for i in range(n):
    p=int(input())
    resposta=""
    if p!=0:
        if p%2==0:
           resposta= resposta+"EVEN"
        else:
           resposta= resposta+"ODD"
        if p>0:
            resposta=resposta+" POSITIVE"
        else:
           resposta= resposta+" NEGATIVE"
    else:
        reposta="NULL"
    print resposta




