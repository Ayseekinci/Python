# Kullanıcıdan kısa kenarı alıp uzun kenarıda=18 alıp dikdörtgenin çevresini ve alanını hesaplanması
class dikdortgen:

    kisakenar = int(input("Kısa kenar : "))
    def __init__(self, uzunkenar=18):
        self.uzunkenar = uzunkenar

    def cevre_hesapla(self):
        return 2*(self.kisakenar+self.uzunkenar)

    def alan_hesapla(self):
        return self.kisakenar + self.uzunkenar


cevre = dikdortgen()
alan = dikdortgen()

print(f"Cevre : {cevre.cevre_hesapla()}")
print(f"Alan : {alan.alan_hesapla()}")


# Soruları kontrol etme

class soru():
    def __init__(self, test, secenek, cevap):
        self.test = test
        self.secenek = secenek
        self.cevap = cevap

    def cevap_kontrol(self, cevap):
        return self.cevap == cevap


soru1 = soru('En iyi programlama dili', [
             'c++', 'java', 'python', 'c#'], 'python')
soru2 = soru('En büyük sayı hangisi ', ['5', '21', '14', '63'], '63')

print(soru1.cevap_kontrol('c++'))
print(soru2.cevap_kontrol('63'))
