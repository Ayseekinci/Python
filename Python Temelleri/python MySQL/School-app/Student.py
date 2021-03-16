class Student:
    def __init__(self, id, OgrenciNo, Ad, Soyad, DogumTarihi, Cinsiyet, ClassId):
        self.id = id
        self.OgrenciNo = OgrenciNo
        self.Ad = Ad
        self.Soyad = Soyad
        self.DogumTarihi = DogumTarihi
        self.Cinsiyet = Cinsiyet
        self.ClassId = ClassId

    @staticmethod
    def CreateStudent(obj):
        list = []

        if isinstance(obj, tuple):
            list.append(Student(obj[0], obj[1], obj[2],
                                obj[3], obj[4], obj[5], obj[6]))
        else:
            for i in obj:
                list.append(Student(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))

        return list
