import requests

# r = requests.get('http://www.baidu.com')
# print(r.cookies)
# #转换为列表
# for key, value in r.cookies.items()
#     print(key + '=' + value)

response = requests.get('https://www.12306.cn')
print(response.status_code)
#加入SSL证书验证(verify)
response = requests.get('https://www.12306.cn',verify=False)
print(response.status_code)