import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
# uzaktaki bir bilgisayardaki mongodb bağlanma.
# myclient = pymongo.MongoClient(
#     "mongodb+srv://ayseekinci:<yourname>@cluster0.n3gsa.mongodb.net/")
# print(myclient.list_database_names())  # kayıtlı olan dosyaları listeler.

mydb = myclient["node-app"]
mycollection = mydb["products"]
# print(mydb.list_collection_names())


# INSERT
#product = {"name": "Samsung S5", "price": 2500}
# tek bir kayıt eklemek için insert_one kullanırlır.
#result = mycollection.insert_one(product)
# print(result.inserted_id)

# birden fazla kayıt eklemek için insert_many kullanılır.
productlist = [
    {"_id": 1, "name": "Samsung S5", "price": 2500},
    {"_id": 2, "name": "Samsung S6", "price": 3000},
    {"_id": 3, "name": "Samsung S7", "price": 3500},
]
result = mycollection.insert_many(productlist)
print(result.inserted_ids)
