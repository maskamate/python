#Másodfokú

import math, cmath

a = input("kérem adja meg az egyenlet főegyütthatóját: ")

a = float(a)
while a==0:
    print("ez nem lesz másodfokú egyenlet; nem oldom meg.")
    a = input("Kérem a másodfokú egyenlet főegyütthatóját: ")
    a= float(a)

b = input("Kérem az elsőfokú tag együtthatóját: ")
c = input("Kérem a konstans tagot: ")
b = float(b)
c = float(c)

d = b*b-4*a*c
print("A diszkrimináns értéke", d)

if d>=0:
    print("Van valós megoldás.")
    x1= (-b-math.sqrt(d))/(2*a)
    x2= (-b-math.sqrt(d))/(2*a)
    print("Az egyik megoldás ", x1)
    print("Az egyik megoldás ", x2)


név = input("Mi az ős neve? ")
bogyók = int(input("Hány bogyója van? "))

if bogyók < 10:
    minősítés = "zsenge"
elif bogyók > 0:
    minősítés = "nagy koponya"
else:
    minősítés = "gyüjtögető"

print(f'{név} egy {minősítés}')


