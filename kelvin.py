c = float(input("Kérem adja meg hány fok van (C°): "))
k = c + 273.15
print("Jelenlegi hőmérséklet: ", c, " C°")

if 34 > c > 28:
    print("Meleg van.")

elif c > 34:
    print("Kánikula van!")

elif 20 < c <  28:
    print("Kellemes az idő.")

elif 10 < c < 20:
    print("Hideg van.")

elif c < 10:
    print("Nagyon hideg van.")


print ("Ez Kelvinbe átszámolva: ", k, " K")









