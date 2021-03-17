from dbmanager import DbManager
from datetime import datetime
from Student import Student


class App:
    def __init__(self):
        self.db = DbManager()

    def initApp(self):
        msg = "*****\n1-Öğrenci Listesi\n2-Öğrenci Ekle\n3-Öğrenci Güncelle\n4-Öğrenci Sil\n5-Çıkış(E/Ç)"
        while True:
            print(msg)
            islem = input("İşlem Seçiniz")
            if islem == '1':
                self.displayStudents()

            elif islem == '2':
                self.addStudent()

            elif islem == '3':
                self.editStudent()
            elif islem == '4':
                self.deleteStudent()
                pass
            elif islem == 'E' or islem == 'Ç':
                break
            else:
                print("Yanlış Seçim Yaptınız.")

    def displayClasses(self):
        classes = self.db.getClasses()
        for i in classes:
            print(f'{i.id}: {i.name}')

    # Öğrenci Ekler.
    def addStudent(self):
        self.displayClasses()

        ClassId = int(input('Hangi sınıfın bilgileri ?'))
        number = input("Öğrenci Numarası :")
        name = input("Öğrenci Adı :")
        surname = input("Öğrenci Soyad :")
        birthdate = input("Birthdate (YYYY,MM,DD): ")
        gender = input("Cinsiyet (E/K) :")
        student = Student(None, number, name, surname,
                          birthdate, gender, ClassId)

        self.db.addStudent(student)

    def deleteStudent(self):
        self.displayStudents()
        studentid = int(input("Öğrenci İD:"))
        self.db.deleteStudent(studentid)

    # Öğrenci Güncelleme

    def editStudent(self):
        self.displayStudents()
        # ClassId = int(input('Hangi sınıfın bilgileri ?'))
        studentid = int(input("Öğrenci İD:"))
        student = self.db.getStudentById(studentid)
        print(student[0].Ad, student[0].Soyad)

        student[0].Ad = input("Ad:") or student[0].Ad
        student[0].Soyad = input("Soyad:") or student[0].Soyad
        student[0].DogumTarihi = input(
            "Doğum Tarihi(YYYY/MM/DD) :") or student[0].DogumTarihi
        student[0].Cinsiyet = input("Cinsiyet: ") or student[0].Cinsiyet
        # student[0].ClassId = input("Sınıf :") or student[0].ClassId

        self.db.editStudent(student[0])

    # Öğrenci listesi

    def displayStudents(self):
        self.displayClasses()

        ClassId = int(input('Hangi sınıfın bilgileri ?'))
        student = self.db.getStudentsByClassId(ClassId)
        print("Öğrenci Listesi : ")

        for std in student:
            print(f"{std.id}-{std.Ad} {std.Soyad}")


app = App()
app.initApp()
