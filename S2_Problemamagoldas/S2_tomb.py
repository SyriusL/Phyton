import random

while True:
    x=int(input("Kérem adja meg az oszlopok számát"))
    if x>0:
        break

while True:
    y=int(input("Kérem adja meg az sorok számát"))
    if y>0:
        break
    
A=[]

for sor in range(y):
    s=[]
    for oszlop in range(x):
        r=random.randint(-100,100)
        s.append(r)
    A.append(s)

for s in A:
    print(s)