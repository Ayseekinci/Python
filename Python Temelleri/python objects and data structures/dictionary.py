        #ORNEK 1 :Hasta kayıt formu :::



hastalar={}

kimlik =input("Hastanın tc kimlik numarası : ")
name =input("Hastanın adı : ")
surname =input("Hastanın soyadı : ")
birth=input("Hastanın doğum tarihi : ") 

hastalar[kimlik]={

    'Ad':name,
    'Soyad':surname,
    'Dogumgunu' :birth
  
}

print(hastalar)






      #ORNEK 2 :  : Ogrenci kayıt yenileme ve listede öğrenci arama ::

Ogrenci={}

no =input("Öğrenci okul numarası : ")
name =input("Öğrencinin adı : ")
surname =input("Öğrencinin soyadı : ")
address=input("Öğrencinin adresi : ") 

Ogrenci.update({

    no:{

    'Ad':name,
    'Soyad':surname,
    'Adres' :address }
  
})
no =input("Öğrenci okul numarası : ")
name =input("Öğrencinin adı : ")
surname =input("Öğrencinin soyadı : ")
address=input("Öğrencinin adresi : ") 

Ogrenci.update({

    no:{

    'Ad':name,
    'Soyad':surname,
    'Adres' :address }
  
})
no =input("Öğrenci okul numarası : ")
name =input("Öğrencinin adı : ")
surname =input("Öğrencinin soyadı : ")
address=input("Öğrencinin adresi : ") 

Ogrenci.update({

    no:{

    'Ad':name,
    'Soyad':surname,
    'Adres' :address }
  
})

print(Ogrenci)

ogrNo=input('Öğrenci numarasını giriniz :')
Ogrenci1=Ogrenci[no]
print(Ogrenci1)

    


   
   #ORNEK 3   Kullanıcı yazdırma ::


   users= {

    'AyseEkinci':{
    'yas ':23,
    'dogumtarihi':1998,
    'telefon':5649795265,
    'adres':'Adiyaman'
    },
   
    'CinarKaya':{
    'yas':40,
    'dogumtarihi':1981,
    'telefon':25495684664,
    'adres':'Ankara'

    }

}
print(users['AyseEkinci']['adres'][3])
print(users['CinarKaya']['telefon'])





