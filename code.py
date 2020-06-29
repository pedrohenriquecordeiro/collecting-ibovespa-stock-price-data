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
print(tbody)


# get tr in tbody
trs = handle_all_components_by_tag_name(tbody, 'tr')
print(trs)

'''
# loop in row of table
for tr in trs:
    a = handle_component_by_xpath(
        tr, '/td[2]/a'
    )
    stock_name = a.get_attribute('textContent')
    print(stock_name)

'''

driver.quit()
