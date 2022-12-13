import numbers
import random

a = 5
b = random.randint(5,25)
c = int(input("Kérlek adj meg egy számot: "))

print("a = ",a)
print("b = ",b)
print("c = ",c)

#d feladat
print("A három szám összege: ", a + b + c)
print("A három szám szorzata: ", a * b * c)

szorzat = a * b * c

if szorzat > 500:
    print("A számok szorzata nagyobb mint 500")
else:
    print("A számok szorzata kisebb mint 500")

if (c%2):
    print('A c szám páratlan')




