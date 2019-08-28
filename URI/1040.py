# -*- coding: utf-8 -*-
n1,n2,n3,n4=raw_input().split(" ")
n1=float(n1)
n2=float(n2)
n3=float(n3)
n4=float(n4)
media=(2*n1+3*n2+4*n3+n4)/10
print "Media: %.1f" %media
if media>=7.0:
    print "Aluno aprovado."
else:
    if media<5:
        print "Aluno reprovado."
    else:
        print "Aluno em exame."
        ne=float(input())
        print "Nota do exame: %.1f" %ne
        media =(media+ne)/2
        if media>=5:
            print "Aluno aprovado."
        else:
            print "Aluno reprovado."
        print "Media final: %.1f" %media
