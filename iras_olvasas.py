with open('10Ef.txt', 'w', encoding = 'utf-8') as file:
    file.write('csordasne kovacs judit')

wr = open('10e2f.txt', 'w')
wr.write('csordasne kovacs judit')
wr.close()

re = open ('10Ef.txt', 'r')
line = re.readline
print(line)
re.close


re = open('10Ef.txt', 'r')
line = re.readline()
while line != "":
    line = line.strip()
    print(line)
    line = re.readline()
re.close()


re = open("adat.txt", "r")
line = re.readline()
while line !="":
    line = line.strip()
    datas = line.split()
    print("%s/%s/%s/%s ="% \
        (datas[0], datas[1],
         datas[4], datas[2],
         datas[3]))
    line = re.readline()
re.close()