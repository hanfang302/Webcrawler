#selenium模拟登录
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from fake_useragent import UserAgent

driver = webdriver.Chrome(executable_path='/home/bc/桌面/chromedriver')
driver.get('https://douban.com')
#显示等待，目的为了等待页面全部加载完毕
driver.implicitly_wait(10)
driver.find_element_by_id('form_email').send_keys('18518753265')
driver.find_element_by_id('form_password').send_keys('ljh123456')
driver.find_element_by_class_name('bn-submit').click()
print(driver.get_cookies())
driver.get('')
print(driver.s)

cookie_str = ''
for cookie in driver.get_cookies():
    print(type(cookie))
    cookie_str += cookie['name']+cookie['value']+'; '

ua = UserAgent()
print(cookie_str[:-2])
headers = {
    'User-Agent':ua.chrome,
    'cookie':cookie_str,
}


# driver = webdriver.Chrome(executable_path='/home/bc/桌面/chromedriver')
# driver.get('https://weibo.com')
# #显示等待，目的为了等待页面全部加载完毕
# driver.implicitly_wait(10)
# driver.find_element_by_id('form_email').send_keys('')
# driver.find_element_by_id('form_password').send_keys('')
# driver.find_element_by_class_name('bn-submit').click()

