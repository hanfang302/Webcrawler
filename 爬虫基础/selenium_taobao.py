from selenium import webdriver
#from selenium.webdriver.common.keys import keys
import time

browse = webdriver.Chrome(executable_path='/home/bc/桌面/chromedriver')
#模拟浏览器发起一个 请求
browse.get('https://www.taobao.com')
#渲染后的浏览器页面信息
print(browse.page_source)
#如何输入模拟用户输入
browse.find_element_by_id('q').send_keys('美食')
#模拟用户点击按钮
browse.find_element_by_xpath('//div/button[@class="btn-search tb-bg"]').click()
browse.implicitly_wait(5)
time.sleep(5)
#模拟点击下一页      
browse.find_elements_by_class_name('n')[0].click()
browse.find_element_by_class_name('n').click()
time.sleep(5)
#模拟前进
#browse.forward()
#模拟后退
#browse.back()
#关闭所有
browse.close()
# #退出
browse.quit()

#def main():
    
