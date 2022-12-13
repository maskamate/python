#5c
# Naponta legalább 2,5 liter folyadékot kell fogyasztanunk,
# és ivásból nem vagyunk valami jók.  Írjunk programot,
# amelyik bekéri, hogy egy-egy alkalommal hány decit ittunk!
# Teszi mindezt addig, amíg 0 értéket nem adunk meg.
# Minden bekéréskor kiírja, hogy addig hány litert ittunk összesen,
# és ha elérjük a 2,5 litert, akkor erről is megemlékezik.
# 3,5 liter fölött kilép, szépen elbúcsúzva tőlünk

össz = 0

while össz <= 35 and (ivás:=int(input("Hány decit ittál? "))):
    print(f'Már {(össz:=össz+ivás)/10:3.1f} litert ittál.')
    if össz >= 25:
        print("Már sikerült elérned a 2,5 litert.")
print("Béka nől a hasadba\'!'")