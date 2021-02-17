# Yeni gelen ürünleri sisteme kaydetme örneği.

urunler = []

adet = int(input("Kaç adet ürün geldi : "))
i = 0
while i < adet:
    urunadi = input("Ürünün adını giriniz : ")
    fiyat = int(input("Ürünün fiyatını giriniz : "))
    urunler.append({
        'Urun ': urunadi,
        'Fiyat ': fiyat
    })
    i += 1

for urun in urunler:
    print(f"Ürünün adı : {urunadi}  Ürünün fiyatı : {fiyat} ")


# yas hesaplama

dogumyil = [int(input("Doğum yılınızı giriniz : "))]
yas = [2021-dogum for dogum in dogumyil]
print(yas)
