zestaw_1=[]
a=int(input("Podaj liczbę:"))
import random
zestaw_1 =[random.randint(1,10) for i in range(a)]
print(zestaw_1)
zestaw_2 =[random.randint(5,15) for i in range(a)]
print(zestaw_2)
n=int(input("Liczba:"))
if n in zestaw_1 and zestaw_2:
    print("Liczba z zestawu 1")
elif n in zestaw_2:
    print("Liczba z zestawu 2")
elif n in zestaw_1:
    print("Liczba jest w obydwóch zestawach:")
else:
    print("Nie ma takiej liczby w zestawach")
zestaw_1_2=zestaw_1 + zestaw_2
print(zestaw_1_2)
zestaw_1_2.sort()
print(zestaw_1_2)