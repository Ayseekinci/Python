# Personel listesi oluşturup işten ayrılan ve yeni gelen personel güncellemesi örneği.

# class
class personel:
    # class attributes
    address = 'Adres bulunmamakta'

    # constructor(yapıcı metod)
    def __init__(self, name, year):
        # object attributes
        self.adi = name
        self.dogumyili = year


# object
personel1 = personel('Ayşe Ekinci', 1998,)
personel2 = personel('Yağmur Kaya', 1975)
personel3 = personel('Enes Öner', 1990)
personel4 = personel('Ahmet Türk', 1982)

# updating
personel1.adi = 'Şeyma'
personel2.address = 'Muş'
personel3.address = 'İstanbul'
personel4.year = 1979

# accessing object attributes
print(f'Adı : {personel1.adi}   Doğum yılı : {personel1.dogumyili}   Adres : {personel1.address}')
print(f'Adı : {personel2.adi}   Doğum yılı : {personel2.dogumyili}   Adres : {personel2.address}')
print(f'Adı : {personel3.adi}   Doğum yılı : {personel3.dogumyili}   Adres : {personel3.address}')
print(f'Adı : {personel4.adi}   Doğum yılı : {personel4.dogumyili}   Adres : {personel4.address}')
