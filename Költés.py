#Költés

kedd=input("Menyit költöttél kedden? ")
szerda=input("Menyit költöttél szerdán? ")

if kedd > szerda:
    print("Kedden töltöttél többet, ", kedd, "forintot")

elif szerda > kedd:
    print("Szerdán költöttél többet, ", szerda, "forintot")

else:
    print("Ugyan annyit költöttél a két nap")
