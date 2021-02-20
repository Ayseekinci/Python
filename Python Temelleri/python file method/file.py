# encoding="utf-8" türkçe karakter kullanılabilir.
# "w" (write) : yazma modu.
result = open("yeni_dosya.txt", "w")  # yeni dosya oluşturur.
print(result)
# "r" (read) : okuma modu.
file = open("yeni_dosya.txt", "r")
print(file)
# "x" (create) : oluşturma .
# "a" (append) : ekleme.

with open("yeni_dosya.txt", "r+") as file:
    content = file.read()   # tüm dosyaları okur
    file.seek(10)  # istediğin konuma gönderebiliyorsun. 10. konuma gönderilmiş
    print(content)
    print(file.tell())  # klasörün o an ki konumunu verir."""


with open("yeni_dosya.txt", "r+", encoding="utf-8") as file:
    file.seek(5)  # 5. konumdaki yazıyı deneme yapar
    file.write("Deneme ")  # ilk kısmı deneme diye değiştirir.
with open("yeni_dosya.txt", "r+", encoding="utf-8") as file:
    print(file.read())


with open("yeni_dosya.txt", "r+", encoding="utf-8") as file:
    dizi = file.readlines()   # içerikleri dizi şeklinde yazdırır.
    print(dizi)
with open("yeni_dosya.txt", "r+", encoding="utf-8") as file:
    print(file.read())


# Klasörün sonuna isim ekleme
with open("yeni_dosya.txt", "r+", encoding="utf-8") as file:
    file.write("a")
    print("Emel turan")


# Klasörün başına isim ekleme
with open("yeni_dosya.txt", "r+", encoding="utf-8") as file:
    basaekle = file.read()
    basaekle = "Yeni isim \n"+basaekle
    print(basaekle)


# Klasörün ortasına isim ekleme
with open("yeni_dosya.txt", "r+", encoding="utf-8") as file:
    liste = file.readlines()
    liste.insert(1, "Ortaya ekleme")
    file.seek(0)
    for i in liste:
        file.write(i)
with open("yeni_dosya.txt", "r+", encoding="utf-8") as file:
    print(file.read())
