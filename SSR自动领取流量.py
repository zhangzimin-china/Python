
import yagmail
import time
import requests
from selenium import webdriver


url = 'https://liulissr.org/auth/login'
options = webdriver.ChromeOptions()


res = requests.get(url, verify=False)
# res=requests.get(url)
print(res.text)

options.add_argument('--ignore-certificate-errors')
webdriver = webdriver.Chrome(options=options)
# webdriver=webdriver.Chrome()
webdriver.get(url)
print(webdriver.page_source)

element = webdriver.find_element_by_id('email')
element.send_keys('641945043@qq.com')


element = webdriver.find_element_by_id('passwd')
element.send_keys('zhang19961029')

element = webdriver.find_element_by_id('login').click()

time.sleep(3)



ele = webdriver.find_element_by_id('days-account-expire')
webdriver.execute_script("arguments[0].scrollIntoView();", ele)  # 下拉页面至按钮

# element = webdriver.find_element_by_css_selector('.btn.btn-brand.btn-flat').click()  # 点击获取经验按钮
element = webdriver.find_element_by_id('checkin').click()

time.sleep(2)

webdriver.get_screenshot_as_file(r'D:\python\pythonfile\3.png')

webdriver.quit()

yag = yagmail.SMTP(user='zhangzimin1996@163.com',
                   password="XBASUEDLZDOAPNJC", host='smtp.163.com')


yag.send('641945043@qq.com', subject='流量领取', contents='截图',
         attachments=r'd://python//pythonfile//3.png')
