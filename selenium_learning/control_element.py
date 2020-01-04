
from selenium import webdriver
import time

webdriver_path = '/Users/pineapple/Python_Project/selenium_learning/chromedriver'
wd = webdriver.Chrome(webdriver_path)

wd.get('http://www.baidu.com')

# tap something into input box
wd.find_element_by_id('kw').send_keys('selenium')
# click element
wd.find_element_by_id('su').click()

# get attribute of element


wd.close()







