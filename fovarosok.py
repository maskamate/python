import random


fovarosok = []
fovarosok = ["Bécs", "Bern", "Párizs", "London", "Budapest", "Varsó", "Prága", "Róma", "Madrid", "Helsinki", "Moszkva"]
főváros = None
while főváros !='':
    print('fővárosok jelenleg: ', ", ".join(fovarosok))
    főváros = input('Kérek egy fővárost! ')
    if főváros !='':
        fovarosok.append(főváros)

n = random.randint(1,len(fovarosok)-1)

for index, főváros in enumerate(fovarosok):
    print(index, főváros)



while len(fovarosok)>0:
    print('fővárosaink: ', ', '.join(fovarosok))
    melyik = input("Melyik főváros a legszebb, válaszd ki! ")
    if melyik in fovarosok:
        fovarosok.remove(melyik)
    else:
        print("Ilyen város nincs a listába")
