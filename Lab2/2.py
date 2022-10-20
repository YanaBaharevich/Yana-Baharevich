x=input("Podaj literę: ")
if len(x) > 1 or len(x)== 0:
    print('Niepoprawne dane')
    exit()
if x >= 'a' and x <= 'z':
        print("mała litera")
elif 'A' <= x <= 'Z':
        print("DUŻA LITERA")
else:
        print("pozostałe znaki")
