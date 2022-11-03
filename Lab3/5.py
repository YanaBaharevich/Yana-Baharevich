n = int(input("podaj liczbe studentow: "))
x = 1
s = 0
while True:
    p=int(input(f"podaj liczbe punktow studenta {x}: "))
    if p > 100 or p < 0:
        continue
    x=x+1
    s =s+p
    if (n+1==x):
        break
print("srednia punktow wynosi:", round(s/n,2) )