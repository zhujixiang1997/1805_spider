# -*- coding: utf-8 -*-  
__author__ = 'zhougy'
__date__ = '2018/12/19 下午4:35' 

'''
采用selenium进行动态页面的下拉操作
'''
import time
from bshead import create_bs_driver

driver = create_bs_driver()

url = "https://www.toutiao.com/"

driver.get(url)

time.sleep(2)

driver.save_screenshot("1.png")

#execute_script --- 采用selenium执行js脚本
js_script = "window.scrollTo(10000, 20000)"
driver.execute_script(js_script)

time.sleep(5)

driver.save_screenshot("2.png")


js_script = "window.scrollTo(20000, 30000)"
driver.execute_script(js_script)

time.sleep(5)
driver.save_screenshot("3.png")


cookies = driver.get_cookies()
print(f"cookies:{cookies}")

time.sleep(10)
driver.quit()
















