#Henger Felszín és Térfogat

# from platform import mac_ver

import random
m = random.randint(2,10)
r = random.randint(2,10)
# r = int(input("Kérlek add meg a henger sugarát: "))
# m = int(input("Kérlek add meg a henger magasságát: "))
print("A magasság: ", m)
print("A sugár: ", r)

p = 3.14159

#térfogat
v = (r*r*p*m)

#felszín
a = ((2*p*r)*m)+((p*r**2)*2)

print("Térfogat: ", v)
print("Felszín: ", a)