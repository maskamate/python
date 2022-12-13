fok = float(input("Kérem adja meg testének hőfokát: "))
nevek=[]
laz=[]
for _ in range(3):
    nev = input("Kérem adja meg a nevét ")
    nevek.append(nev)
    laz.append(fok)
print(nevek)
print(laz)

if fok <= 36.9:
    print("Nincs láza")

elif 37 < fok < 37.5:
    print("Önnek hőemelkedése van")

elif 37.5 < fok < 38.9:
    print("Önnek láza van")

elif 39 < fok:
    print("Önnek magasláza van")




