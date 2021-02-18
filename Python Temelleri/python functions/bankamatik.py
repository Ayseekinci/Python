# Bankamatik örneği

AyseHesap = {
    'Ad': 'Ayşe Ekinci',
    'Hesapno': 125647,
    'Bakiye': 4000,
    'EkHesap': 2000

}


def paracek(hesap, miktar):
    print(f"Merhaba {hesap['Ad']} ")

    if (hesap['Bakiye'] >= miktar):
        print("Paranızı alabilirsiniz.")
    else:
        toplam = hesap['Bakiye']+hesap['EkHesap']
        if toplam >= miktar:
            ekhesapkullanimi = input('Ek hesap Kullanılsın mı ? (Evet/Hayır) ')

            if ekhesapkullanimi == 'Evet':
                print("Paranızı Alabilirsiniz.")
            else:
                print(
                    f"{hesap['Hesapno']} Nolu hesabınız da {hesap['Bakiye']} bulunmaktadır.")
        else:
            print("Üzgünüz bakiye yetersiz..")


paracek(AyseHesap, 7000)
