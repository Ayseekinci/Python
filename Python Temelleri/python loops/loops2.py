# sayı tahmin etme
import random

sayi = random.randint(1, 50)
hak = 3

while hak > 0:
    hak -= 1
    tahmin = int(input("Bir sayi tahmin ediniz : "))
    if sayi == tahmin:
        print("Tebrikler bildiniz.. ")
        break
    elif tahmin > sayi:
        print("Lütfen daha düşük bir sayı giriniz.")
    else:
        print("Lütfen daha yüksek bir sayı giriniz.")

    if hak == 0:
        print(f"Hak : {hak} Üzgünüm hakkınız bitti.. ")


# Faktöriyel hesaplama

sayi = int(input("Faktoriyeli alınacak sayıyı giriniz: "))
deger = 1
fak = 1
if sayi == 0:
    print(f"{sayi} :1")
else:
    while deger <= sayi:

        fak *= deger
        deger += 1

    print('Faktöriyel sonuc :', fak)
