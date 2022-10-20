x=input("Podaj literę: ")
if len(x) > 1 or len(x)== 0:
    print('Niepoprawne dane')
    exit()

if x >= 'a' and x <= 'z':

        print(x)
elif 'A' <= x <= 'Z':
        print(x)
else:
        print("pozostałe znaki")
