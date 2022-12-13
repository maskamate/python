liter = 0
max = 3,5

while liter !=max:
    deci = int(input("Hány dl folyadékot ittál meg: "))
    liter += deci/1000
    print("Ennyi folyadékot ittál meg: ", liter, "l")

    if deci == 0:
        print("0-át nem fogadom el")
        break

    if liter == 2.5:
        print("2,5 literes cél teljesítve!")

if liter == max:
    print("Viszláááát!")
