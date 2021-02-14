# kendini tanıt tanıtıkttan sonra soyadını başa al.
name = 'Ayşe'
surName = 'Ekinci'
age = 36

print("My name is {} {} and years old {} .".format(name, surName, age))
print("My name is {b} {a} and years old {c} .".format(a=name, b=surName, c=age))

print(f"My name is {name} {surName} and year old {age}") # .format kullanmadan sadace başa f ekleyerek yapılır.

#karenin alanını bulup 3 boşluk ile ilk 5 sayıyı yazdırma örneği

kenar= 0.256789314

alan = 4 * kenar

print(f'alan {kenar: 3.5}')
