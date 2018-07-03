#帮助我们随机获取useragent
from fake_useragent import UserAgent

ua = UserAgent()
print(ua.chrome)
print(ua.ie)
print(ua.random)