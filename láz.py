def laz (hom):
    if hom > 37.5:
        return True
    else:
        return False

nev = None
while nev != ' ':
     nev = input("Kérem adja meg a beteg nevét: ")
     if nev:
        hom = float(input("Kérem adja meg a hőmérsékletét: "))
        if laz(hom):
            print(f'{nev} lázas ')
        else:
            print(f'{nev} nem lázas')
    