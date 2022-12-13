# nev = input("Kérem adja meg a nevét ")
# print(nev)
# ÉV =2022
# udv = (f'Üdvözöllek {nev}')
# print(udv, "szép napot kívánok neked", sep = " ")
# eletkor = int(input("kérem adja meg születési évét "))
# eletk = ÉV- eletkor
# print(eletk)

# if eletk < 15:
#     print("Ön Általános iskolás")
# elif 15 < eletk < 18:
#     print("Ön középiskolás")
# elif eletk > 18:
#     print("Ön Felnőtt")




nev = input("Kérem adja meg a nevét ")
auto = input("Kérem adjon meg egy autómárkát ")
orszag = input("Kérem adja meg a gyártó ország nevét ")
sebesség = int(input("Kérem adja meg az autó végsebességét "))

# print(nev, "által választott autó adatai")
# print(auto)
# print(orszag, "ban gyártják")
# print(sebesség, "km/h")

mondat1 = orszag + ' vidékein készül a(z) ' + auto + ', ami ' + str(sebesség) + 'km/h-val is képes menni'
print (mondat1)

mondat2 = '{}vidékein készül ami {} km/h végsebességre képes'.format(o=orszag, a=auto, s=sebesség)

mondat3a = '{o} vidékein készül, a {a} ami {s} km/h képes.'.format(o=orszag, s=sebesség, a=auto)

print(f'(orszag=), (auto=), (sebesség=)')