'''Prog tételek csoportosítása
Egy sorozathoz egy érték
'''
'''
t = [3, 8, 2, 4, 5, 1, 6]

osszeg = 0
for num in t:
    osszeg = osszeg + num

print ("Összeg: ", osszeg)

szorzat = 1
for num in t:
    osszeg =osszeg + num
    szorzat = szorzat*num
print("Összeg = ", osszeg)
print("Szorzat", szorzat)


t1 = ["d","f","g","h","j","k","l"]
megszámol = len(t)
count = 0
for num in t: 
    if num > 5:
        count = count+1

print("5-nél nagyobb: ", count)


n = len(t)
ker = 5

i = 0
while i < n and [i] != ker:
    i = i + 1

if i < n:
    print("Van ilyen: ", ker)
    print("Nincs ilyen: ", ker)


t = [3, 8, 2, 4, 5, 1, 6]
n = len(t)
ker = 5

i = 0
while t[i] != ker:
    i = i + 1

print("Hányadik helyen van: ", i+1)
'''

roka = [2,5;4,6,7,2,3,4]
osszeg = 0
for num in roka:
    osszeg = osszeg + num
    if i in roka:
print(osszeg)

