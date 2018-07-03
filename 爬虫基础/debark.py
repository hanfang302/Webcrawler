from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lxml import etree
import time

url = 'https://github.com/login'
driver = webdriver.Chrome(executable_path='/home/bc/桌面/chromedriver')
driver.get(url)
time.sleep(5)
driver.find_element_by_id('login_field').send_keys('hanfang123@aliyun.com')
driver.find_element_by_id('password').send_keys('hf980222')
#driver.find_element_by_class_name('btn btn-primary btn-block').click()
driver.find_element_by_xpath('.//*[@name="commit"]').click()

# cookies = driver.get_cookies()
# cookies = ''
# for cookie in cookies:
#     cookies += cookie['name']+cookie['value']+'; '
# with open('cookies.html','w') as f:
#     f.write(cookies[:-1])

