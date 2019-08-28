# -*- coding: utf-8 -*-
a,b=raw_input().split(" ")
b=int(b)
tabela={"1":4,"2":4.5,"3":5,"4":2,"5":1.5}
total=b*tabela[a]
print "Total: R$ %.2f" %total
