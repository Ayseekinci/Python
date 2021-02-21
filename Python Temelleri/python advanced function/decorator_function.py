# dekoratör fonksiyonları
"""
def yeni_dekorator(fonksiyon):
    def islem():
        print("Fonksiyondan öncesi")
        fonksiyon()
        print("Fonksiyondan sonrası")
    return islem


@yeni_dekorator
def isim():
    print("Ayşe Ekinci")
isim()
"""


# islem yapılsın ve yapılan işlemlerinde zamanını hesaplayan örnek


import math
import time


def hesap_zaman(func):
    def ic_hesap(*args):
        basla = time.time()
        func(*args)
        bitis = time.time()
        print("fonksiyon" + str(bitis-basla)+"saniye sürdü.")

    return ic_hesap


@hesap_zaman
def usalma(x, y):
    print(math.pow(x, y))


@hesap_zaman
def faktoriyel(sayi):
    print(math.factorial(sayi))


usalma(3, 2)
faktoriyel(4)
