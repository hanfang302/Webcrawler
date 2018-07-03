import pymongo
#链接mongo数据库（本地连接）
client = pymongo.MongoClient('127.0.0.1',27017)
client = pymongo.MongoClient('localhost',27017)
#远端连接
client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
#如何查询获取数据库
article_db = client.article
#如何获取数据库下面的集合
nove1 = article_db.nove1
#查询所有数据库文档
result = nove1.find()
for dict in result:
    print(dict)
#print(result)
# #获取第一条数据
# result = nove1.find_one()
# print(result)

# #如果数据库存在就获取，不存在就创建
# db = client.student
# #如果集合存在就获取，不存在就创建
# student = db.student
# document = {
#     'name':'lisi',
#     'age':'20',
#     'class':'201',
#     'hight':170,
# }

# document1 = {
#     'name':'lisi1',
#     'age':'22',
#     'class':'202',
#     'hight':175,
# }

# document2 = {
#     'name':'lisi2',
#     'age':'23',
#     'class':'203',
#     'hight':180,
# }

# #表示插入数据
# #result = student.insert(document)
# #result = student.insert([document,document1,document2])
# #返回的结果是一个列表
# #[ObjectId('5b29b7a281512d18440561e8'), ObjectId('5b29b7a281512d18440561e9'), ObjectId('5b29b7a281512d18440561ea')]
# #print(result)

# #获取集合中所有数据
# # result = student.find()
# # for dict in result:
# #     print(dict)

# #获取一条数据
# result = student.find_one()
# #条件查询
# result = student.find({'name':'lisi1'})
# for dict in result:
#     print(dict)
# print(result)

# #获取第一条满足条件的数据
# result = student.find_one({'name':'lisi1'})
# print(result)
# #跳过第一条数据，获取后两条数据
# result = student.find().skip(1).limit(2)
# for dict in result:
#     print(result)
# #更新数据
# result = student.update({'name':'lisi2'},{'$set':{'hight':165}})
# print(result)
# #查看更新结果是否正确
# result = student.find_one({'name':'lisi2'})
# print(result)
# #排序(升序)
# result = student.find().sort('age',1)
# #降序
# result = student.find().sort('age',-1)
# for dict in result:
#     print(dict)

# #save跟update的区别：如果update跟新
