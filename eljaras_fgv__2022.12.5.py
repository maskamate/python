'''
#ELJÁRÁS PARAMÉTER NÉLKÜL

def border():
    print()
    for i in range(80):
        print("-", sep='', end='')
    print('\n')

print("1. Feladat")
border()
print("3. Feladat")
border()
print("4. Feladat")
border()
print("6. Feladat")


#ELJÁRÁS PARAMÉTERADÁSSAL

def border(n,s):
    print()
    for i in range (n):
        print(s, sep='', end='')
    print('\n')

border(80, '*')
print("1. Feladat")
print("a) Feladat")
border(10, "-")
print("b) Feladat")
border(80, '*')
print("2. Feladat")



# VÁLTOZÓK HATÓKÖRE

def proc():
    global a
    a = 5
    print(b)
    c = 3
    print(c)



b = 0
c = 4
proc()
print(a)


# ÉRTÉK SZERINTI PARAMÉTERADÁS
def proc(x):
    x += 1
    print(x)

proc(3)
a = 10
proc(a)
print(a)



def pn(num):
    end = int(num/2)
    s = 1
    for i in range(2, end+1):
        if num % i == 0:
            s += i
    if s == num:
        print(" Tökéletes szám")
    else:
        print(" Nem tökéletes szám")

for i in range(2,1001):
    print(i, end = "")
    pn (i)
ob = int(input("Kérem a vizsgálandószámot: "))
pn(ob)


def red(t, w, l):
    if l <= 25 or w <= 15:
        t = 0.8 * t
    return t

t = int(input("Kérem adja meg a kedvezmény nélküli adót: "))
l = int(input("Kérem a telek hosszát: "))
w = int(input("Kérem a telek szélességét: "))
print("A kedvezményes adó: ", red(t,w,l))
'''

def hetnapja(honap,anp):
    napnev = ["Vasárnap", "Héfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat"]
    napszam = [0, 31, 59, 90, 120, 151, 101, 212, 243, 273, 304, 335]
    napsorszam = (napszam[honap=1]+nap) % 7
    return napnev[napsorszam]

print(hetnapja(1,0))
