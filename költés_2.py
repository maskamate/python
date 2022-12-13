kedd = int(input("Hány forintot költöttél kedden? "))
szerda = int(input("Hány forintot költöttél szerdán? "))

if kedd > szerda:
    print(f'Kedden többet költöttél, {kedd} forintot')

elif szerda > kedd:
    print(f'Szerdán többet költöttél, {szerda} forintot')

else:
    print(f'A két nap ugyan annyit költöttél')