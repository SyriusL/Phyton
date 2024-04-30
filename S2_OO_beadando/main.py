from datetime import datetime

class Szoba:
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 10000)  # Például az árakat egyszerűsítettük

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 15000)  # Például az árakat egyszerűsítettük

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []

    def add_szoba(self, szoba):
        self.szobak.append(szoba)

class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

    def get_ar(self):
        return self.szoba.ar

class FoglalasKezelo:
    def __init__(self):
        self.foglalasok = []

    def foglalas(self, szoba, datum):
        # Ellenőrizd, hogy a dátum jövőbeli-e és a szoba elérhető-e
        if datetime.now() < datum and szoba not in [foglalas.szoba for foglalas in self.foglalasok]:
            foglalas = Foglalas(szoba, datum)
            self.foglalasok.append(foglalas)
            return True
        else:
            return False

    def lemondas(self, foglalas):
        if foglalas in self.foglalasok:
            self.foglalasok.remove(foglalas)
            return True
        else:
            return False

    def listaz(self):
        return self.foglalasok

# Szálloda, szobák és foglalások inicializálása
szalloda = Szalloda("Hotel Luna*****")
szalloda.add_szoba(EgyagyasSzoba(101))
szalloda.add_szoba(KetagyasSzoba(201))
szalloda.add_szoba(KetagyasSzoba(202))

foglalaskezelo = FoglalasKezelo()
foglalaskezelo.foglalas(szalloda.szobak[0], datetime(2024, 5, 1))
foglalaskezelo.foglalas(szalloda.szobak[1], datetime(2024, 5, 2))
foglalaskezelo.foglalas(szalloda.szobak[2], datetime(2024, 5, 3))

# Felhasználói interfész
print("Üdvözöljük a", szalloda.nev, "szállodában!")
while True:
    print("\nVálasszon műveletet:")
    print("1. Foglalás")
    print("2. Lemondás")
    print("3. Foglalások listázása")
    print("4. Kilépés")

    valasztas = input("Válasszon: ")

    if valasztas == "1":
        # Foglalás
        szobaszam = int(input("Adja meg a foglalni kívánt szoba számát: "))
        datum_str = input("Adja meg a foglalás dátumát (YYYY-MM-DD formátumban): ")
        datum = datetime.strptime(datum_str, "%Y-%m-%d")

        szoba = None
        for sz in szalloda.szobak:
            if sz.szobaszam == szobaszam:
                szoba = sz
                break

        if szoba:
            if foglalaskezelo.foglalas(szoba, datum):
                print("Foglalás sikeres.")
            else:
                print("A foglalás sikertelen.")
        else:
            print("Nincs ilyen szoba.")

    elif valasztas == "2":
        # Lemondás
        print("A következő foglalások érhetők el:")
        for i, foglalas in enumerate(foglalaskezelo.listaz()):
            print(i+1, "-", foglalas.szoba.szobaszam, "-", foglalas.datum.strftime("%Y-%m-%d"))

        lemondas_idx = int(input("Adja meg a lemondani kívánt foglalás sorszámát: ")) - 1
        if lemondas_idx >= 0 and lemondas_idx < len(foglalaskezelo.foglalasok):
            foglalas = foglalaskezelo.foglalasok[lemondas_idx]
            if foglalaskezelo.lemondas(foglalas):
                print("Lemondás sikeres.")
            else:
                print("A lemondás sikertelen.")
        else:
            print("Érvénytelen sorszám.")

    elif valasztas == "3":
        # Foglalások listázása
        print("A foglalások:")
        for foglalas in foglalaskezelo.listaz():
            print(foglalas.szoba.szobaszam, "-", foglalas.datum.strftime("%Y-%m-%d"))

    elif valasztas == "4":
        # Kilépés
        print("Köszönjük, hogy használta a szolgáltatásunkat!")
        break

    else:
        print("Nem érvényes választás. Kérem válasszon újra.")
