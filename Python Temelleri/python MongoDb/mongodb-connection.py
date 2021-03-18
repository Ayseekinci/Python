import pymongo
from bson import ObjectId

myclient = pymongo.MongoClient("mongodb://localhost:27017")

# uzaktaki bir bilgisayardaki mongodb bağlanma.......
# myclient = pymongo.MongoClient(
#     "mongodb+srv://ayseekinci:<yourname>@cluster0.n3gsa.mongodb.net/")

# print(myclient.list_database_names())  # kayıtlı olan dosyaları listeler.

mydb = myclient["node-app"]
mycollection = mydb["products"]
# print(mydb.list_collection_names())


# INSERT......
# product = {"name": "Samsung S5", "price": 2500}
# tek bir kayıt eklemek için insert_one kullanırlır.
# result = mycollection.insert_one(product)
# print(result.inserted_id)


# birden fazla kayıt eklemek için insert_many kullanılır......
# productlist = [
#{"name": "Samsung S5", "price": 2500, "description": "Kötü telefon"},
#{"name": "Samsung S7", "price": 3000},
#{"name": "Samsung S8", "price": 3500},
#{"name": "Samsung S9", "price": 4000, "description": "İyi Telefon"},
#{"name": "Samsung S10", "price": 4500},
#{"name": "Samsung S11", "price": 5000}

# ]
#result = mycollection.insert_many(productlist)
# print(result.inserted_ids)


# FIND(tek kayıt getirme)......
# result = mycollection.find_one()  # bulduğu ilk kaydı getirir.
# print(result)


# FIND(çoklu kayıt getirme)......
# for i in mycollection.find():#hepsini gösterir.

# for i in mycollection.find({}, {"_id": 0, "name": 1}):  # sadece name yazdırır.
# 0=gösterme 1=göster.
# print(i)


# Fitreleme İşlemi......
# result = mycollection.find_one({"_id": ObjectId('6053c124978cad94e04f1a6e')})#id göre sorgulama işlemi.
# print(result)

# result = mycollection.find({
# "name": {
#   " $in": ["Samsung S5", "Samsung S4"]}#bu bilgilere ait kayıt varsa yazdırır.
# })

# result = mycollection.find({
# "price":  # {"$gt": 2500}#fiyatı 2500 den büyük olanlar
# {"$gte": 3000}  # fiyatı 3000 den büyük ve eşit olanlar
# {"$lt": 3000}  # fiyatı 3000 den küçük olanlar
# {"$lte": 3000}  # fiyatı 3000 den küçük ve eşit olanlar

# })
# result = mycollection.find({
# "name": {"$regex": "^S"}  # name kısmında 'S' ile başlayanlar})
# for i in result:
# print(i)


# SORT Sorgusu......

# result = mycollection.find().sort("name")#name kolonuna göre alfabetik sıralama yapar.
# result = mycollection.find().sort("name", -1)# name kolonuna göre alfabetik sıralamayı terster yapar.
# for i in result:
# print(i)


# UPDATE......

# mycollection.update_one(
# {"name": "Galaksi S15"},
# {"$set": {
# "name": "Iphone 7",
# "price": 8000}}
# )
# for i in mycollection.find():
# print(i)


# DELETE......
# mycollection.delete_one({"name": "Samsung S5"})#Tek bir kayıt siler.

# mycollection.delete_many({"name": {"$regex": "I"}})#I harfiyle başlayanları siler.

for i in mycollection.find():
    print(i)
