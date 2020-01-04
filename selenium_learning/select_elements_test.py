from selenium import webdriver
import time

webdriver_path = '/Users/pineapple/Python_Project/selenium_learning/chromedriver'
wd = webdriver.Chrome(webdriver_path)

wd.get('http://www.baidu.com')


# by element id
wd = webdriver.Chrome(webdriver_path)
wd.get('http://www.baidu.com')
wd.implicitly_wait(10)

query_element = wd.find_element_by_id('kw')
query_element.send_keys('selenium')

click_element = wd.find_element_by_id('su')
click_element.click()
time.sleep(10)
wd.close()

# by class
wd = webdriver.Chrome(webdriver_path)
wd.get('http://f.python3.vip/webauto/sample1.html')

animal_element = wd.find_elements_by_class_name('animal')
for animal in animal_element:
    print(animal.text)
wd.close()

# by tag
wd = webdriver.Chrome(webdriver_path)
wd.get('http://f.python3.vip/webauto/sample1.html')

tag_element = wd.find_elements_by_tag_name('span')
for tag in tag_element:
    print(tag.text)

wd.close()

# by web element
wd = webdriver.Chrome(webdriver_path)
wd.get('http://f.python3.vip/webauto/sample1.html')

container_element = wd.find_element_by_id('container')
span_element = container_element.find_elements_by_tag_name('span')
for span in span_element:
    print(span.text)
wd.close()