hofok = int(input("Kérem adja meg a hőfkot"))
hofok = float(input("Kérem adja meg a hőfkot"))

olvadási = 1539 °C
forrási = 2750  °C


if hofok < olvadási:
    print("Szilárd")
elif hofok < forrási:
    print("Folyékony")
else:
    print("Gáz")

    