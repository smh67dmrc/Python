# -*- coding: cp1254 -*-

print "Bu Program Girilen Metinde Hangi Harfin Ka� Tane Oldu�unu G�sterir."

a = raw_input("L�tfen Bir Metin Giriniz: ")
def uniq(input):
  output = []
  for x in input:
    if x not in output:
      output.append(x)
  return output
c = uniq(a)
for b in c:
    print b , "=====>" , a.count(b) , "adet bulundu."


