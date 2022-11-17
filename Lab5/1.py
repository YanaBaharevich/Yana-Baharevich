values = [10,20,33]
keys=["ten", "twelwe", "thirty"]
print(values)
print(keys)
print(list(zip(values,keys)))

z1=dict(zip(values,keys))
print(z1)

z1={}
for i in range(len(values)):
    z1[keys[i]]=values[i]
print(z1)

z2=dict(thirty=30,fourty=40,fifty=50)
print(z2)
print()
z3=z1.copy()
z3.update(z2)
print(z3)