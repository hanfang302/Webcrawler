import requests
import re
#转换为
import json
#http://www.mogujie.com/
#获取的首页为空,但是网页上出现了，说明数据肯定通过接口
#获取大分类

#发送get请求
response = requests.get('http://mce.mogucdn.com/jsonp/multiget/3?callback=jQuery211039274210603581894_1528697416261&pids=110119&_=1528697416262')
print(response.text)
#方案one
pattern = re.compile("jQuery.*?\((.*?)\)")
json_data = re.findall(pattern,response.text)[0]
#方案two
#json_data = response.text[41:-1]
print(json_data)
#json.loads转换为python对象
data = json.loads(json_data)
print(type(data))
big_ategory = data['data']['110119']['list']
print(big_ategory)
print(len(big_ategory))

#循环这个获取到的列表里的每一个值，并且添加到pids这个空的列表中
pids = []
for item in big_ategory:
    # print(item)
    pids.append(item['categoryPid'])
# #拼接数组里的每一个元素
pids = ','.join(pids)
print(pids)

#获取全部分类
#取二级分类所有菜单
url = 'http://mce.mogucdn.com/jsonp/multiget/3'
parmas = {
    'callback':'jQuery211039274210603581894_1528697416261',
    'pids':pids,
    '_':'1528697416262'
}
response = requests.get(url,params=parmas)
#print(response.text)
#获取括号里的内容
all_category_json = re.findall(pattern,response.text)[0]
#print(all_category_json)
all_category_data = json.loads(all_category_json)
print(type(all_category_data))
all_category_dict = all_category_data['data']
#59行路径的正则匹配
category_pattern = re.compile(r'http.*?/(\d+).*?acm',re.S)
#分类
category_list = []
user_category = []

for k,v in all_category_dict.items():
    #print(k)
    #获取分类的值
    for sub_dict in v['list']:
        #print(sub_dict['title'])
        print(sub_dict['title'],sub_dict['link'])
        #路径
        id = re.findall(category_pattern,sub_dict['link'])[0]
        #print(id)
        dict = {
            title:id[0]
        }
        user_category.append(title)
        category_list.append(dict)
print('尊敬的用户您可以从一下列表中筛选您的商品:'+'\n'+str(user_category))
#kw键
kw = input('输入您要选择的商品分类:')
startpage = int(input('请输入起始页:'))
endpage = int(input('请输入终止页:'))
category_id = ''
for sub_dict in category_list:
     category_id = sub_dict[kw]
#url = 'https://s10.mogucdn.com/__/mfp/meili-base-logger/assets/1.3.2/logger.min.js'
for i in range(startpage,endpage+1):
url = 'http://list.mogujie.com'

#print(category_list)