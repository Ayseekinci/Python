
# iç içe işlev kullanımı (Kapsülleme)
def dis_fonk(sayi1):
    print('dis_fonk')

    def ic_fonk(sayi1):
        print('ic_fonk')
        return sayi1 + 1
    sayi2 = ic_fonk(sayi1)
    print(sayi1, sayi2)


dis_fonk(10)


def faktoriyel(sayi):

    def ic_faktoriyel(sayi):
        if sayi <= 1:
            return 1
        return sayi*ic_faktoriyel(sayi-1)
    return ic_faktoriyel(int(sayi))


print(faktoriyel(6))


# 1 den büyük sayıların üssünü alma örneği
def usalma(sayi):

    def ic_fonsk(ussu):
        if sayi >= 1:
            return sayi**ussu

    return ic_fonsk


us = usalma(4)
print(us(3))


# dört işlem örneği


def islem(islem_adi):
    def toplam(*args):
        toplama = 0
        for i in args:
            toplama += i
        return toplama

    def cikarma(*args):
        cikar = 0
        for i in args:
            cikar -= i
        return cikar

    def carpma(*args):
        carpim = 1
        for i in args:
            carpim *= i
        return carpim

    def bolme(*args):
        bol = 1
        for i in args:
            bol *= i
        return bol

    if islem_adi == 'toplama':
        return toplam
    elif islem_adi == 'cikarma':
        return cikarma
    elif islem_adi == bolme:
        return bolme
    else:
        return carpma


toplama = islem('toplam')
print(toplama(1, 3, 5, 6))
cikarma = islem('cikarma')
print(cikarma(2, 3, 8, 4,))
carpma = islem('carpma')
print(carpma(1, 2, 3, 6, 4))
bolme = islem('bol')
print(bolme(21, 3, 7,))
