
bejutott = False

while not bejutott:
    felhasznalonev = input("Add meg a felhasználóneved: ")
    jelszo = input("Kérem adja meg a jelszavát: ")
    if felhasznalonev == 'bori99' and jelszo == 'kismehe<3':
        print('a belépés megengedve')
        bejutott = True
    else: 
        print('belépés megtagadva')