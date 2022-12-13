m = float(input("Kérem adja meg a magasságát (cm): "))
s = float(input("Kérem adja meg a súlyát (kg): "))
bmi = s / (m ** 2) *10000

print("Az ön magassága: ", m, " cm")
print("Az ön súlya: ", s, " kg")
print(bmi)

if 20.5 < bmi < 26.5:
    print("Az ön osztályzása: Normális") 

elif 26.6 < bmi < 31.9:
    print("Az ön osztályzása: Túlsúly")

elif 32.0 < bmi < 36.9:
    print("Az ön osztályzása: I.fokú elhízás")


elif 37.0 < bmi < 41.9:
    print("Az ön osztályzása: II. fokú elhízás")

elif bmi > 42:
    print("Az ön osztályzása: III. fokú elhízás")