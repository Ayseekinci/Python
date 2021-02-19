# Personel listesi oluşturup işten ayrılan ve yeni gelen personel güncellemesi örneği.

class personel:
    address = 'Adres bulunmamakta'

    def __init__(self, name, year):
        self.adi = name
        self.dogumyili = year


personel1 = personel('Ayşe Ekinci', 1998,)
personel2 = personel(name='Yağmur Kaya', year=1975)
personel3 = personel(name='Enes Öner', year=1990)
personel4 = personel(name='Ahmet Türk', year=1982)

personel1.adi = 'Şeyma'
personel2.address = 'Muş'
personel3.address = 'İstanbul'
personel4.year = 1979

print(f'Adı : {personel1.adi}   Doğum yılı : {personel1.dogumyili}   Adres : {personel1.address}')
print(f'Adı : {personel2.adi}   Doğum yılı : {personel2.dogumyili}   Adres : {personel2.address}')
print(f'Adı : {personel3.adi}   Doğum yılı : {personel3.dogumyili}   Adres : {personel3.address}')
print(f'Adı : {personel4.adi}   Doğum yılı : {personel4.dogumyili}   Adres : {personel4.address}')
