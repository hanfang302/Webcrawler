# sudo service mongodb start 启动mongodb
# sudo service mongodb stop 关闭mongodb
# mongo(db) 启动mongodb数据库
# db 查看当前数据库
# show dbs 查看所有数据库
# use + 数据库名 表示切换数据库 
# db.createCollection('集合名称')创建一个集合
# db.集合名称.insert({'key':'value'})插入一个文本(值)
# db.集合名称.find() 显示所有数据
# db.dropDatabase()删除数据库
# db.集合名称.drop() 删除一个集合
# db.集合名称.update({条件},{$set:设置需要修改的内容})局部修改
# db.集合名称.update({条件},{设置修改的内容})全局修改
# updat会覆盖同样的数据，没有数据不会插入
# db.集合名称.save()保存和insert功能相仿没有数据会插入数据
# db.集合名称.find().skip().limit()跳过数据,limit显示数据条数
# db.集合名称.find().sort({'key':})序列排列
# db.集合名称.distinct('去重字段',{条件})消除重复数据
# db.集合名称.find({条件文档}).pretty()将所有数据格式化
# db.集合名称.find({'条件':{$regex:''}i})regex正则匹配(字符串)
# db.集合名称.remove({'key':'value'})#删除单条数据
# db.集合名称.aggregate([{$group:{_id:'',条件:{$sum:'$'}}}])_id:根据什么字段去分组
# quit()退出
# exit退出