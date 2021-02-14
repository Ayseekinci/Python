# kendini tanıt tanıtıkttan sonra soyadını başa al.
name = 'Ayşe'
surName = 'Ekinci'
age = 36

print("My name is {} {} and years old {} .".format(name, surName, age))
print("My name is {b} {a} and years old {c} .".format(a=name, b=surName, c=age))

print(f"My name is {name} {surName} and year old {age}") # .format kullanmadan sadace başa f ekleyerek yapılır.



#karenin cevresini bulup 3 boşluk ile ilk 5 sayıyı yazdırma örneği

kenar= 0.256789314

cevre = 4 * kenar

print(f'cevre {cevre: 3.5}')
