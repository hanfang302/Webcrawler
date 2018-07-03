#post请求
import requests

#拉钩https://www.lagou.com/gongsi/
#目标url
url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
data = {
    'first':'false',
    'kd':'php',
    'pn':'1',
}
header = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'coookie':'WEBTJ-ID=20180606101146-163d2dd4404406-03ca32f1d9e1f6-3b7c015b-670800-163d2dd44051f4; _ga=GA1.2.1911489333.1528251107; user_trace_token=20180606101142-f42cb4c1-692e-11e8-9379-5254005c3644; LGUID=20180606101142-f42cba72-692e-11e8-9379-5254005c3644; _gid=GA1.2.1496238956.1528251119; JSESSIONID=ABAAABAAADEAAFI04BCEC5F459FFC1BAB9DE10CD2F5E0A1; LGSID=20180606101215-0858a710-692f-11e8-9379-5254005c3644; PRE_UTM=; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DFgtFRBBnd_skTeg8y7WfZdv77UyH5L1BY6Flt7ey5rbPxeQNDjEQZlIkHVf5y0vf%26wd%3D%26eqid%3Ddb8bf5800000238f000000035b1742fa; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fgongsi%2F; _gat=1; index_location_city=%E5%85%A8%E5%9B%BD; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1528251657,1528251676,1528252278,1528252293; TG-TRACK-CODE=search_code; SEARCH_ID=80a7ab0e862e480dbb14a173f878fb5c; LGRID=20180606103233-de2cd4a0-6931-11e8-923d-525400f775ce; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1528252358',
    'Referer':'https://www.lagou.com/jobs/list_php?labelWords=&fromSearch=true&suginput=',
    'Host': 'www.lagou.com',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Anit-Forge-Token': 'None',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
}
response = requests.post(url,data=data,headers=header)
print(response.status_code)
#print(response.text)
#使用json()可以直接将一个json字符串转换为Python的对象一般要么是字典，要么是list(数组)
data = response.json()
print(data['content']['hrInfoMap']['2305269'])
print(type(data))

#