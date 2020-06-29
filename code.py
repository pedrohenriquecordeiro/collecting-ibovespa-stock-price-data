from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
TIMESTAMP = 10

driver = webdriver.Chrome('chromedriver') 
driver.get('https://br.investing.com/equities/')
time.sleep(10)
driver.quit()
