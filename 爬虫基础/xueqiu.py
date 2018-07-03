import requests
import ssl

header = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',

}
requestContent = ssl._create_unverified_context()
response = requests.get('',headers=header,context=requestContext)
print(response.text)

#1.找到分类
#2.找ajax接口
#https://xueqiu.com/v4/statuses/public_timeline_by_category.json?since_id=-1&max_id=20289503&count=15&category=-1

#数据层结构
data = {
    'list':[
        {},
        {},
        {}
    ]
}
data['list']
