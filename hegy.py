hegy1=int(input('Add meg a hegynek a magasságát méterben! '))
hegy2=int(input('Add meg a másik hegynek a magasságát méterben! '))

def km1(hegymászóm1):
    return(hegymaszom1/1000)

def név1(hegymászó1):
    return(hegymaszo1.upper())

def előnév(hegymászó1): 
    if hegymaszo1[0].lower() in mgnhangzók:
        return("az")
    else:
        return('a')       
        
if hegy1 > hegy2:
    print("Az első hegy az magasabb mint a második.")
    wr.write(f"Az első hegy az magasabb mint a második.")
elif hegy1 < hegy2:
    print("Az első hegy az kisebb mint a második.")
    wr.write("Az első hegy az kisebb mint a második.")
else:
    print("A két hegy magassága megegyezik.")
    wr.write("A két hegy magassága megegyezik.")
    
for _ in range(3):
    hegymaszo1=input('Mi az első hegymászó neve? ')   
    hegymaszom1=int(input('Mi az első hegymászónak megtett magasságának métere? '))
    print(f"{előnév(hegymaszo1)}  {név1(hegymaszo1)} megtett {km1(hegymaszom1)} km-t.")


wr=open("H:\hegy.txt",'W')
wr.write('Add meg a hegynek a magasságát méterben! ')
wr.write('Add meg a másik hegynek a magasságát méterben! ')
mgnhangzók=['a', 'á', 'e', 'é', 'i', 'í', 'o', 'ó', 'ö', 'ő', 'u', 'ú', 'ü', 'ű']