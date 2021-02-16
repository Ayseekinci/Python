#Kullanıcıdan 2 değer alsın bu iki değerler toplamının sonucu pozitif çift sayı olup olmadığını bulsun.

x =float(input('1.Sayı :  '))
y=float(input('2.Sayı : '))
toplam= (x+y)

if (toplam>0):
     if (toplam % 2==0):
         print("Sayı cift. ")
    
     else:
         print("Girilen sayı pozitif ancak Sayı tek.")
   
          
else:
    print(f"Sayı :{toplam } = Negatif. ")



#Kullanıcıdan isim,yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumlarınu kontrol ediniz.
#--Ehliyet alabilme koşulu en az 18 ve eğitim durumu lise ya da üniversite olmalıdır.

isim=(input("Adınız : "))
yas=int(input("Yaşınız : "))
egitim=(input("Eğitim durumu : "))


if (yas>=18):
    if (egitim=='lise' or egitim=='universite'):
        print('aldınız')
    else:
         print('Eğitim durumununuzdan dolayı alamadınız')

else:
    print("Yaşınız tutmadığından dolayı alamadınız....")




# Not ortalaması hesaplama 
#  100-85 =AA 
#  84-70=BB
#  69-50=CC
# 49-0=KALDI

not1=float(input("1.notunuz : "))
not2=float(input("2.notunuz : "))
sozlu=int(input("Sözlü notunuz : "))
ortalama=(not1+not2+sozlu)/3

if (ortalama>=0 and ortalama<=49):
    print(f"Ortama : {ortalama} = KALDINIZ .")
elif (ortalama>=50 and ortalama<=69):
    print(f"Ortalama : {ortalama} = CC")
elif(ortalama>=70 and ortalama<=84):
    print(f"Ortalama : {ortalama} = BB")

else:
    print(f"Ortalama : {ortalama} = AA")




#Email ve parola kontrolü

Email='Ayseekinci.02.00@gmail.com'
parola=2654875

girilenEmail=(input("Email adresini giriniz : "))
girilenParola=int(input("Şifrenizi giriniz : "))

if (girilenEmail==Email):
    print("Eposta adresiniz doğru")
    if(girilenParola==parola):
        print("Parola Doğru")
    else:
        print("Parola Yanlış")
    


else:
    print("Email adresinizi yanlış girdiniz...GİRİŞ GERÇEKLEŞTİRİLEMEDİ..")


        






