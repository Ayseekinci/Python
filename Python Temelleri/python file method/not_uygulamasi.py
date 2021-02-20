def not_hesapla(satir):
    satir = satir[:-1]
    liste = satir.split(':')
    ogrenciad = liste[0]
    notlar = liste[1].split('.')

    not1 = int(notlar[0])
    not2 = int(notlar[1])

    ortalama = (not1 + not2)/2
    print(ortalama)


def ortalamaları_oku():
    with open("sinav_notlari.txt", "r", encoding="utf-8") as file:
        for satir in file:
            print(not_hesapla(satir))


def notlari_gir():
    ogrn_no = input("Öğrenci numarası : ")
    ad = input("Öğrenci ad : ")
    not1 = int(input("1.not : "))
    not2 = int(input("2.not : ")


    with open("sinav_notlari.txt", "r", encoding="utf-8") as file:
        file.write(ogrn_no+''+ad+''+not1+','+not2+',' + '/n')


def notlari_kaydet():
    with open("not_hesapla.txt", "r", encoding="utf-8") as file:
        liste=[]

        for i in file:
            liste.append(not_hesapla(i))

while True:
    islem=input("1=Notları oku  2=Notları gir  3=Notları kaydet")
    if islem == '1':
        ortalamaları_oku()

    elif islem == '2':
        notlari_gir()

    elif islem == '3':
        notlari_kaydet()

    else:
        break
