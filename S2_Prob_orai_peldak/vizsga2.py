def pitagoraszi_szamharomok(veg):
    for a in range(1, veg + 1):
        for b in range(a, veg + 1):
            c = (a**2 + b**2) ** 0.5
            if c.is_integer() and c <= veg:
                print([a, b, int(c)])

def main():
    try:
        veg = int(input("Kérem, adjon meg egy pozitív egész számot, ami nagyobb, mint 5: "))
        if veg < 5:
            print("A megadott szám nem pozitív egész szám, vagy kisebb, mint 5!")
            return
        print(f"A {veg}-ig tartó Pitagoraszi számhármasok:")
        pitagoraszi_szamharomok(veg)
    except ValueError:
        print("Hibás bemenet. Kérem, csak pozitív egész számot adjon meg.")

if __name__ == "__main__":
    main()
