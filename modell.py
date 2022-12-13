def megfelel(magassag):
    if int (magassag)<170:
        return False
    else:
        return True

nev = None
while nev != '':
    nev = input("Add meg a jelentkező nevét ")
    if nev !='':
        m = input('Hány centiméter magas? ')
        if megfelel(m):
            print(nev, "megfelelő magasságú. ")
        else: print(nev,'magassága nem megfelelő modellnek')