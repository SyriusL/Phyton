#hány darab számjegyből áll a szám
def szamjegyekszama(sz):
    db=0
    while sz>0:
        db+=1
        #tört számtag elhagyása az osztás után  549/10  54
        sz=sz//10
    return db

#számjegyek összegének az értéke:
def szemjegyosszeg(sz):
    ertek=0
    while sz>0:
        #a nem egész értéket adja vissza a szám végéről, pl 543,4    4
        ertek=ertek+(sz%10)
        sz=sz//10
    return ertek

#szám fordítottja
def szamjegyforditottja(sz):
    ertek=0
    while sz>0:
        ertek=(ertek*10)+(sz%10)
        sz=sz//10
    return ertek

#tükörszám
def tukorszam(sz):
    return sz == szamjegyforditottja(sz)

def parostorol(sz):
    ertek=0
    while sz>0:
        if sz%2 != 0:
            ertek=(ertek*10)+sz%10
        sz=sz//10
    #meg kell fordítani a végeredményt, hogy a számok az eredeti sorrendben legyenek
    return szamjegyforditottja(ertek)

szam = input('kérek egy számot: ')
print(szamjegyekszama(int(szam)))
print(szemjegyosszeg(int(szam)))
print(szamjegyforditottja(int(szam)))
print(tukorszam(int(szam)))
print(parostorol(int(szam)))



