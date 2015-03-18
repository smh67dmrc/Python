# -*- coding: cp1254 -*-

print "Bu Program Girilen Metinde Hangi Harfin Kaç Tane Olduğunu Gösterir."

a = raw_input("Lütfen Bir Metin Giriniz: ")
def uniq(input):
  output = []
  for x in input:
    if x not in output:
      output.append(x)
  return output
c = uniq(a)
for b in c:
    print b , "=====>" , a.count(b) , "adet bulundu."


