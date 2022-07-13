from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait as wd
from selenium.webdriver.support.expected_conditions import visibility_of_all_elements_located as vis

# driver = webdriver.Chrome("./chromedriver.exe")

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome("./chromedriver.exe",options=options)


driver.get(r'file:///C:/Users/Gowtham%20Theja/Downloads/drive-download-20220705T081121Z-001/loading.html')



driver.find_element_by_name("fname").send_keys("Gowtham")


# driver.get('https://stackoverflow.com/questions/tagged/python%2bpandas?tab=Active')

# links = driver.find_elements_by_class_name("s-link")

# for link in links:
#     print(dir(link))

# driver.get('//C:/Users/Gowtham%20Theja/Downloads/drive-download-20220705T081121Z-001/demo.html')


# options = driver.find_elements_by_xpath('//*[@id="standard_cars"]/option')

# for option in options:
#     print(option.text)

# options = driver.find_elements_by_xpath('//*[@id="standard_cars"]/option')

# for option in options:
#     option.click()
#     sleep(2)

# options = driver.find_elements_by_xpath('//*[@id="standard_cars"]')

# for option in options:
#     if option.text=="Audi":
#         option.click()



# driver.get('http://demowebshop.tricentis.com')

# class PassFail:
#     def __init__(self,price):
#         self.price = price
    
#     def __eq__(self,other):
#         if self.price == other.price:
#             return 'Pass'
#         return 'Fail'

# elements = driver.find_elements_by_xpath('//input[@value="Add to cart"]/../../..//a')

# for i in elements:
#     product = i.text
#     print(product)
#     price = driver.find_element_by_xpath(f'//a[text()="{product}"]/../..//span').text
#     print(price)
#     exp_price = PassFail(25.00)
#     act_price = PassFail(float(price))
#     print(exp_price==act_price)

# elements=driver.find_elements_by_xpath('//img')

# for i in  elements:
#     with open('Logo.png', 'wb') as file:
#         # l = driver.find_element_by_xpath('//*[@alt="Tricentis Demo Web Shop"]')
#         l = driver.find_elements_by_xpath(f'{i}')
#         file.write(l.screenshot_as_png)






# import re
# s = 'aabbccddcccaadd'
# res=""
# l = [ ]
# for i in s:
#     r=tuple(re.findall(f'{i}+',s))
#     l.append(r)
# print(set(l))
    