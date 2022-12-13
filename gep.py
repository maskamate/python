# from ctypes.wintypes import PUSHORT
# from math import radians
# from msvcrt import kbhit


# t = input("Miyen típusú a számítógép: ")
# á = int(input("Mennyibe kerül? "))
# m = input("Működik? (IGEN/NEM) ")

# if á <= 25000 and m == 'igen':
#     print("Megveszem")

# elif á > 25000 and m == 'nem':
#     print("Nem veszem meg")

# if á <= 25000 and m== 'nem':
#     print("Megvesszük")

# elif á > 25000 and m == 'igen':
#     print("Nem veszem meg")


# # print("Az ön által választott gép ára: ", á)
# # print("Valamint típusa: ", t)
# # print("És állapota: ", m)




név = input("Mi a gép neve? ")
működik = True if input("Működik i/n? ") == 'i' else False
ár = int(input("Mi az ára? "))

if (név == "ZX Spectrum" or név == "C64") and működik and ár <=25000:
    print("Biznisz!!!!!")

else:
    print("Gagyi nyócbitesek...Kinek kellenek?!")