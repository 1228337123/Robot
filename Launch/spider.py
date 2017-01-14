from Launch.GetDriver import GetDriver
from pymongo import MongoClient
conn = MongoClient("localhost", 27017)
collection = conn.Sina.spiderdata
collection.insert({"question": 1+1, "answer_one": "2","answer_two": "two"})

# driver = GetDriver().get_driver()   # 注意类实例化要加括号（）
# # driver.get('http://bing.com')
# driver.get('http://neihanshequ.com')