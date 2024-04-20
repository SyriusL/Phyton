import random

while True:
    x=int(input("kérem adja meg az oszlopok számát: "))
    if x>0:
        break

while True:
    y=int(input("kérem adja meg az sorok számát: "))
    if y>0:
        break

#mátrix tábla feltöltése random adatokkal    
A=[]
for sor in range(y):
    s=[]
    for oszlop in range(x):
        s.append(random.randint(-100,100))
    A.append(s)

print(A)

#külön sorba nyomtatás
for s in A:
    print(s)

#minimum érték megkeresése
m=[]
for s in A:
    m.append(min(s))
print(min(m))

#összes elem összeadása
osszertek=[]
for s in A:
    osszertek.append(sum(s))
print(sum(osszertek))

#soronként kiírni az összértéket
print('soronként az összege: ', osszertek)
print('soronként az átlaga: ')
for i in range(y):
    print(osszertek[i]/x)

#soronként a legnagyobb és a legkisebb elem
minik=[]
maxok=[]
sorosszeg=[]
soratlag=[]
for s in A:
    minik.append(min(s))
    maxok.append(max(s))
    sorosszeg.append(sum(s))
    soratlag.append(sum(s)/y)
print(minik)
print(maxok)
print(sorosszeg)
print(soratlag)

