# JSON
import json

person_string = '{"Ad":"Ayşe Ekinci","Diller":["Python,C++"]}'
personel_dict = {"Ad": "Ayse Ekinci", "Diller": ["Python,C++"]}


# json stringi dict çevirme
result = json.loads(person_string)
result = result["Diller"]  # diller bilgini yazdırır.
print(type(result))
print(result)


# Farklı bir dosyanın açıp içerisindeki bilgileri yazdırma örneği.

with open("personel.json") as f:  # personel.json dosyasını bul
    data = json.load(f)  # yükleme işlemi yapar
    # personel.json dosyasının içerisindeki ad kısmını yazdır
    print(data["Ad"])

# Dict den json stringe çevirme
result = json.dumps(personel_dict)
print(result)


# personel klasörüne yeni bilgi ekleme
with open("personel.json", "w") as f:
    json.dump(personel_dict, f)


# Kişisel bilgi düzenli bir şekilde yazdırma
x = {
    "Ad": "Ayşe",
    "age": 23,
    "dogum_tarihi": 1998,
    "universite": [
        {"Adiyaman Universitesi": "Bilgisayar Programciligi"},
        {"Firat Universitesi": "Yazilim Muhendisliği"}
    ]
}

# anahtarları alfabetik olarak sıralamak:
print(json.dumps(x, indent=4, sort_keys=True))  # 4 girintili oluştur
