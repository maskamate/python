import random


def nevelo(szo):
    maganhangzo = "aáeéiíoóöőuúüű"
    if szo[0].lower() in maganhangzo:
        return 'az'
    else:
        return 'a'

def jelszo():
    return random.choice(['piros', 'nagy', 'könnyed'])

print('Adj meg három főnevet! ')
for szam in range(1,4):
    fonev = int(str(szam)+' fonev: ')
    print(nevelo(fonev).capitalize()," ", fonev, '', jelzo(), sep="")