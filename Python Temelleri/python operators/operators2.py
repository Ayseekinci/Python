   #Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.

sayi=int(input("Bir sayi giriniz :"))

kontrol= (sayi>=0 and sayi<=100)
print(f"Girilen sayının kontrolü : {kontrol}")


#Email ve parola bilgileri ile giriş kontrolleri yapınız.

Email='Ayseekinci.02.00@gmail.com'
parola='Abc1235'

girilenEmail=input('Email : ')
girilenParola=input('Parola : ')

resualt=(girilenEmail==Email)
resualt1=(girilenParola==parola)
print(f"Email Bilgisi :{resualt}  Parola Bilgisi : {resualt1}")




#kişinin ad,kilo ve boy bilgilerini alıp kilo indekslerini hesaplayın.
#formul:(kilo / boy uzunluğunun karesi)
#Aşağıdaki kişi hangi gruba girmektedir.
   #0-18.4 :: Zayıf
   #18.5-24.9 :: Normal
   #25.0-29.9 ::Fazla Kilolu
   #30.0-34.9 ::Şişman


ad=input("Adının giriniz : ")
kilo=float(input("Kilonuzu giriniz : "))
boy=float(input("Boyunuzu giriniz : "))

formul= (kilo/(boy**2))
print(formul)
zayif= formul >0 and formul <=18.4
normal= formul >=18.5 and formul<=24.9
fazlakilolu= formul>=25.0 and formul<=29.9
sisman=formul>=30.0 and formul<=34.9


print(f"Adım : {ad} kilomun indeksi :{formul}  Girdiğim grup : {zayif}")
print(f"Adım : {ad} kilomun indeksi :{formul}  Girdiğim grup : {normal}")
print(f"Adım : {ad} kilomun indeksi :{formul}  Girdiğim grup : {fazlakilolu}")
print(f"Adım : {ad} kilomun indeksi :{formul}  Girdiğim grup : {sisman}")