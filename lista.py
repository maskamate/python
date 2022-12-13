kacatok = []

kacat = 'bármi'
while kacat !='elfogyott':
    kacat = input('Kérek egy kacatot! ')
    if kacat != 'elgogyott':
        kacatok.append(kacat)

kacatok_felsorolva = ', '.join(kacatok)
print('A kacatjaim? ', kacatok_felsorolva, '.', sep='')