import random
punkty = []
x=0
for i in range (15):
    a = random.uniform(0, 50)
    a=round(a,2)
    x=round(x, 2)
    punkty.append(a)
    x=x+a
print(punkty)
b=float(input("Podaj punkty:"))
if b in punkty:
    print(punkty.index(b))
else:
    print("Nie ma takich punktów")
print("Maximalna liczba:",max(punkty))
print("Minimalna liczba:",min(punkty))
print("Srednia liczba punktów:", round(x/15,2))
punkty_1=[]
punkty_2=[]
for i in range(15):
 if punkty[i]>x/15:
     punkty_1.append(punkty[i])
 elif punkty[i]<x/15:
     punkty_2.append(punkty[i])
print("powyżej średniej:",punkty_1,len(punkty_1))
print("poniżej średniej:",punkty_2, len(punkty_2))