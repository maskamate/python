#Gyümölcs
barack_menny = int(input("Mennyi barack termett (mázsa) "))
barack_ár = input("Mennyibe fáj a barack? ")

körte_menny = int(input("Mennyi körte termett (mázsa) "))
körte_ár = input("Mennyibe fáj a körte? ")

kg_b=barack_menny*100
kg_k=körte_menny*100
print (barack)

print("A barack ", kg_b, "kg")
print("A körte ", kg_k, "kg")

if kg_b > kg_k:
    print("A barack több")

elif kg_k > kg_b:
    print("a körte több")

