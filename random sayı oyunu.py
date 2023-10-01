import random
sayı = random.randint(0,100)
hak = 10
sayac = 0
while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input("bir değer giriniz:"))
    if sayı == tahmin:
        print(f"Tebrikler {sayac}. defada bildiniz.")
        break
    elif (sayı>tahmin): 
        print("yukarı")
    else:
        print("aşağı")
    if (hak == 0):
        print(f"Hakkınız bitti. Tutulan Sayı: {sayı}")