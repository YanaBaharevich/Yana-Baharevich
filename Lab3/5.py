x=int(input("Proszę dodać liczbę studentów:" ))
y=1  #liczba od której zaczyna się wpisywanie punktów\pierwszy uczeń
n=0  #suma punktów
while (y<=x):
    if x > 0:
        print("Punkty studenta po kolejcy",y,":",end=" ")
        b = int(input())
        y=y+1
        n=n+b
    elif x <= 0:
        print("Niepoprawna liczba")
z=n/x #Średnia liczba punktów w grupie
print("Średnia liczba punktów w grupie: ",z)