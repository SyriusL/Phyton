def oszto_osszeg(szam):
    osszeg = 0
    for i in range(1, szam):
        if szam % i == 0:
            osszeg += i
    return osszeg

def keres_szamok():
    try:
        felhasznalo_szama = int(input("Kérem, adjon meg egy számot: "))
        for szam in range(1, felhasznalo_szama + 1):
            if oszto_osszeg(szam) == szam:
                print(szam)
    except ValueError:
        print("Hibás bemenet. Kérem, csak egész számot adjon meg.")

keres_szamok()
