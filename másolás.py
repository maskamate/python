'''

#másolás
t = [2,4,7,1,8,5,9]
b = []
c = []
d = []
e = []
def dupla(num):
    return num*2

for elem in t:
    b.append(dupla(elem))
    if elem%2 == 0:
        c.append(elem)
    if elem < 5:
        d.append(elem)
    if elem%2 != 0:
        e.append(elem)
print(b)
print(c)

#kiválogatás

print(d)
'''

#buborék rendezés

t = [2,4,7,1,8,5,9]
n = len(t)
for i in range(n-1,0,1):
    for j in range(0,1):
        if(t[j]>t[j+1]):
            tmp = t[j+1]
            t[j+1]=t[j]
            t[j] = tmp
print(t)