'''

Írjon programot tengerszint néven!
Kérjen be addig földrajzi hely nevét és tengerszint feletti magasságát, 
amíg üres karaktert nem üt a felhasználó!

Írjon függvényt!
a tengerszintek néven, amely alföldet,"dombságot,"középhegység" és "magashegység" különböztet meg!
200m alatt alföldet,
200m és 500m között dombságot
500m és 1500m között középhegység
1500m magashegység


# Fájl írása tenger.txt néven az amelyben az összes eredmény szerepel!

Beadandó

A program forráskódja .py kiterjesztéssel a Githubra!
A program forráskódja .txt kiterjesztéssel dkt-ra!

'''

foldr = input("Kérem adja meg a földrajzi helyet: ")
tengersz = int(input("Kérem adja meg a tengerszintet: "))

print(f"A tengerszint: {tengersz}, {foldr}-ban(-ben)")

if tengersz < 200:
    print("Alfold")
elif tengersz >200 and 500:
    print("Dombság")
elif tengersz >500 and 1500:
    print("Hegység")
else:
    print("Magashegység")