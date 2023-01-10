class Híres_auto:
    def __init__(self, márka_név, henger_térfogatát, nemzetiseg):
        self.név = márka_név
        self.henger_térfogat = henger_térfogatát
        self.nemzetiseg = nemzetiseg

    def get_nemzetiség(self):
        if self.nemzetiseg == "J":
            return "Japán"
        elif self.nemzetiseg == "N":
            return "Német"


hires_autok = []
for i in range(1):
    marka_nev = input("Addja meg a márka nevét: ")
    henger_terfogat = (input("Addja meg a henger térfogatát: "))
    nemzetiseg = input("Addja meg a márka nemzetiségét: ")
    hires_auto = Híres_auto(marka_nev, henger_terfogat, nemzetiseg)
    hires_autok.append(hires_auto)

for hires_auto in hires_autok:
    print(f' A {hires_auto.marka_nev}, "egy híres" , {hires_auto.get_nemzetiseg()}, "márka", {hires_auto.henger_terfogat}')
