import time
import datetime

from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

MAXIMUM_TIME = 20 # 20 seconds

driver = webdriver.Chrome('chromedriver') 
driver.get('https://br.investing.com/equities/')

# waiting the website load
time.sleep(MAXIMUM_TIME)
driver.implicitly_wait(MAXIMUM_TIME)

# getting tbody of stocks
tbody = WebDriverWait(driver, MAXIMUM_TIME).until(
    EC.presence_of_element_located(
        (
            By.XPATH, 
            '/html/body/div[6]/section/div[8]/table/tbody'
        )
    )
)

# getting tr in tbody
trs = tbody.find_elements_by_tag_name('tr')

# header of csv file
header = ''
prices = ''

# getting header
for tr in trs:
    # anchor tag
    a = tr.find_element_by_tag_name('a')
    stock_name = a.get_attribute('textContent')
    if 'ON' in stock_name: # only stock ON
        header = str(header) + ';' + str(stock_name)

# writting header of csv file
with open('stocks_today.csv', 'a') as stock_file:
    stock_file.write(header[1:] + '\n')

# looping in rows of table
while(True):
    # getting prices
    for tr in trs:
        # anchor tag
        a = tr.find_element_by_tag_name('a')
        stock_name = a.get_attribute('textContent')

        if 'ON' in stock_name:  # only stock ON
            # td tag
            td_last_price = tr.find_element_by_xpath('//td[3]')
            last_price = td_last_price.get_attribute('textContent')
            prices = str(prices) + ';' + str(last_price) 

    with open('stocks_today.csv', 'a') as stock_file: # saving in file csv
        stock_file.write(prices[1:] + '\n')
    
    print(prices[1:] + '\n')
    prices = ''  # cleaning up

    time.sleep(60 * 10) # 10 minutes
    print('Waiting ...')

driver.quit()
