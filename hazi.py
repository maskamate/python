reggeli = {'víz', 'kenyér', 'tojás'}
ebed = {'halászlé','tészta','leves'}

print(reggeli | ebed)
print(reggeli ^ ebed)
print(reggeli - ebed)
print(reggeli & ebed)

gyumolcskosar = ['eper','alma','szilva','eper']
fajta = set()
for gyumolcs in gyumolcskosar:
    fajta.add(gyumolcs)
print(fajta)