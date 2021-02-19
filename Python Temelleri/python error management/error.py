
# print(a)  # => NameError
# int('5sa64')  # => ValueError
# print(25/0)   # => ZeroDivisionError
# print('denem'e)  # => SyntaxError

try:
    a = int(input("a değerini giriniz : "))
    b = int(input("b değerini giriniz : "))

    print(a/b)
except ZeroDivisionError:
    print("Lütfen b değerine '0' rakamını kullanmayınız.")

except ValueError:
    print("Lütfen girdiğiniz değer sayı değeri olsun. ")


# Kullanıcı bilgileri doğru girene kadar sor.
while True:
    try:
        sayi1 = int(input("Sayi1 = "))
        sayi2 = int(input("Sayi2 = "))
        print(sayi1+sayi2)
    except Exception as yanlis:
        print("Yanlış bilgi girdiniz : ")
    else:
        break
print("Doğru bilgi girdiniz.")
