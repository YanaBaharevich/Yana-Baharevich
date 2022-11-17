import random
elementy = []
for i in range (10):
    a = random.randint(0,100)
    elementy.append(a)
print(elementy)
for i in range(3):
 x=elementy[9:6]
 elementy[0:3] = []
 elementy.insert(i,x)
print(elementy)