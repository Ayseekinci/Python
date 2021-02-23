import requests

import json


# gitmek istediğimiz internet  adresi
result = requests.get("https://www.w3schools.com/python/python_ref_list.asp")
result = result.text  # sayfanın html içerdiği kısmı yazdır
print(result)


api_url = "https://api.exchangeratesapi.io/latest?base="
bozulan_doviz = input("Hangi döviz türünü bozmak istiyorsunuz : ")
alinan_doviz = input("Hangi döviz türünü almak istiyorsunuz : ")
miktar = int(input(f"Ne kadar {bozulan_doviz} bozdurmak istiyorsunuz : "))
result = requests.get(api_url+bozulan_doviz)
result = json.loads(result.text)

print("1 {0} ={1} {2}".format(bozulan_doviz,
                              result['rates'][alinan_doviz], alinan_doviz))
print("{0}{1}={2}{3}".format(miktar, bozulan_doviz,
                             miktar*result['rates'][alinan_doviz], alinan_doviz))


class Github:
    def __init__(self):
        self.api_url = "https://api.github.com"

    def kullanicial(self, kullaniciadi):
        response = requests.get(self.api_url+'/Kullanicilar/'+kullaniciadi)
        return response.json()

    def kodkismi(self, kullaniciadi):
        response = requests.get(
            self.api_url+'/Kullanicilar/'+kullaniciadi+'/depo/')
        return response.json()


Github = Github()
while True:
    secim = input(
        "1-Kullanıcı \n2-Kod Kısmı \n3-Çık\nSECİM:")

    if secim == '3':
        break
    else:
        if secim == '1':
            kullaniciadi = input('Kullanıcı adı : ')
            result = Github.kullanicial(kullaniciadi)
            print(result)
        elif secim == '2':
            kullaniciadi = input("Kullanıcı adı giriniz : ")
            result = Github.kullanicial(kullaniciadi)
            for depo in result:
                print(depo['name'])

        else:
            print("Yanlış Seçim Yaptınız.. ")
