from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from datetime import date, datetime

try:
    start_time = datetime.now()
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logger"])
    driver = webdriver.Chrome(options=options, executable_path='D:\Tech_M\iTAP\chromedriver.exe')
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    steps='' 
    message=''

    driver.implicitly_wait(20)
    element = driver.find_element_by_xpath('//input[@name="user-name"]')
    element.send_keys('standard_user')
    steps += "\n" + "test_step_input"+ element.text
    driver.implicitly_wait(20)
    element = driver.find_element_by_xpath('//input[@name="password"]')
    element.send_keys('secret_sauce')
    steps += "\n" + "test_step_input"+ element.text
    driver.implicitly_wait(20)
    element = driver.find_element_by_xpath('//input[@name="login-button"]')
    steps += "\n" +"test_step_click" + element.text
    element.click()
    driver.implicitly_wait(20)
    element = driver.find_element_by_xpath('//button[@name="add-to-cart-sauce-labs-bolt-t-shirt"]')
    steps += "\n" +"test_step_click" + element.text
    element.click()
    driver.implicitly_wait(20)
    element = driver.find_element_by_xpath('//button[@name="add-to-cart-sauce-labs-fleece-jacket"]')
    steps += "\n" +"test_step_click" + element.text
    element.click()
    driver.implicitly_wait(20)
    element = driver.find_element_by_xpath('//button[@name="add-to-cart-sauce-labs-backpack"]')
    steps += "\n" +"test_step_click" + element.text
    element.click()
  
    
    with open("logfile.log", "w+") as external_file:
        finish_time = datetime.now()
        total = finish_time - start_time
        total=str(total).split(".")[0]
        final = "total time taken : " + total
        external_file.write("test passed - no errors" + "\n" +steps + "\n"+message+"\n" + final )
    driver.close()
except Exception as e:
    print(e)
    finish_time = datetime.now()
    total = finish_time - start_time
    total=str(total).split(".")[0]
    path = open("logfile.log", 'w+')
    path.write("failed:\n"+ str(e) + '\n' + steps + " \n total time taken : "+total)
    path.close()
    driver.close()
