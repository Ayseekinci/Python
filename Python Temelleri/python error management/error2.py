# Parola oluşturma
def Parolakontrol(prl):
    import re
    if len(prl) < 7:
        raise Exception("Lütfen 7 karakterden fazla giriniz.")
    elif not re.search("[a-z]", prl):
        raise Exception("Parola küçük harf içermelidir.")
    elif not re.search("[0-9]", prl):
        raise Exception("Parola rakam içermelidir.")

    elif re.search("/s", prl):
        raise Exception("Parola boşluk içermemelidir.")
    else:
        print("Geçerli parola..")


parola = '125864a'
try:
    Parolakontrol(parola)

except Exception as ex:
    print(ex)


liste = ["5", "18", "1as", "a6s", "27", "32"]

# liste içindeki sayısal değerleri bulunuz.
for x in liste:
    try:
        result = int(x)
        print(result)
    except ValueError:
        print("Hatalı değer")

# Kullanıcı 'q' değerini girmedikçe aldığınız her inputun sayı oladuğuna emin olun
# aksi takdirde hata mesajı versin.

while True:
    sayi = input("Sayı : ")
    if sayi == 'q':
        break
    try:
        result = float(sayi)
        print("Giridiğiniz sayi ", result)
        break
    except ValueError:
        print("Geçersiz sayi .")
