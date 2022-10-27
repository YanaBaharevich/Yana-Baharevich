a=int(input("pierwsza liczba:" ))
b=int(input("druga liczba:" ))
if (a > b):
 a,b = b,a

while (a <= b):
    if a % 2 == 1:
        a=a+1
        continue
    print(a, end=" ")
    a = a + 1