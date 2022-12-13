szo1 = input("Adj meg egy szót: ")
szo2 = input("Adj meg egy másik szót: ")
szo1_van = szo1.find('e')
szo2_van = szo2.find('e')

if szo1_van > 0 and szo2_van >0:
    print('oké')
else:
    print("nem jó")