import requests
import re 
import json
import csv
import pymysql

#获取所有 的分类
def get_all_category():
    response = requests.get('http://mce.mogucdn.com/jsonp/multiget/3?callback=jQuery211039274210603581894_1528697416261&pids=110119&_=1528697416262')
    print(response.text)
    #创建一个正则对象，匹配返回结果的json字符串
    pattern = re.compile(r'jQuery.*?\((.*?)\)')
    #匹配出json字符串
    json_data = re,findall(pattern,response.text)[0]
    print(json_data)
    #根据json.loads将json字符串转换为oython对象
    data = json.loads(json_data)
    #打印转换后的参数类型
    print(type(data))
    #取大部分的分类列表
    big_ategory = data['data']['110119']['list']
