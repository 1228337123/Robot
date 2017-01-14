from pymongo import MongoClient
conn = MongoClient("localhost", 27017)
db = conn.Sina

# 2 查询一条数据
# 假设在testdb下有一个名为col的collection
# print(db.Fans.find_one())
#
# # 3 遍历所有数据
# for item in db.Fans.find():
#     print(item)

# 4
# db.Fans.insert({"_id": 21, "1": "Neal","2": "Nea2"})