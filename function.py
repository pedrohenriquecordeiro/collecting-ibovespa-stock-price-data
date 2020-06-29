from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TIMESTAMP = 10

def handle_component_by_xpath(driver, xpath):
    try:
        component = WebDriverWait(driver, TIMESTAMP).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        return component
    except:
        print('\n[ERROR: can not find:' + str(xpath) + ']\n')
        return None


def handle_component_by_tag_name(driver, tag_name):
    try:
        component = WebDriverWait(driver, TIMESTAMP).until(
            EC.presence_of_element_located((By.TAG_NAME, tag_name))
        )
        return component
    except:
        print('\n[ERROR: can not find:' + str(xpath) + ']\n')
        return None


def handle_all_components_by_class_name(driver, class_name):
    try:
        components = WebDriverWait(driver, TIMESTAMP).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, class_name))
        )
        return components
    except:
        print('\n[ERROR: can not find:' + str(class_name) + ']\n')
        return None


def handle_all_components_by_tag_name(driver, tag_name):
    try:
        components = WebDriverWait(driver, TIMESTAMP).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, name))
        )
        return components
    except:
        print('\n[ERROR: can not find:' + str(tag_name) + ']\n')
        return None
