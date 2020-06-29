import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from functions import *

driver = webdriver.Chrome('chromedriver') 
driver.get('https://br.investing.com/equities/')

time.sleep(30)
driver.implicitly_wait(30)

# get tbody of stocks
tbody = handle_component_by_xpath(
    driver,
    '/html/body/div[6]/section/div[8]/table/tbody'
)

# get tr in tbody
trs = tbody.find_elements_by_tag_name('tr')

# loop in row of table
for tr in trs:
    a = tr.find_element_by_tag_name('a')
    stock_name = a.get_attribute('textContent')
    td_last_price = tr.find_element_by_xpath('//td[3]')
    last_price = td_last_price.get_attribute('textContent')

    print(stock_name,last_price)



driver.quit()
