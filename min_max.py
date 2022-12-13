wr = open('max.txt', 'w')
t = [2,4,7,1,8,5,9]
wr.write(f't = [2,4,7,1,8,5,9]')
maxElem = t[0]
for elem in t:
    if elem > maxElem:
        maxELem = elem
print(f'{maxElem}\n')
wr.write(f'{maxELem}\n')

wr.close

#min
wr = open('max.txt', 'w')
t = [2,4,7,1,8,5,9]
wr.write(f't = [2,4,7,1,8,5,9]')
minElem = t[0]
for elem in t:
    if elem < minElem:
        minElem = elem
print(f'{minElem}\n')
wr.write(f'{minElem}\n')  