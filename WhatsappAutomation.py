from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import  By
import time



driver.get("https://web.whatsapp.com")
time.sleep(10)

search_box= driver.find_element_by_class_name('_2zCfw')
search_box.send_keys('Papa'+Keys.ENTER)

text_box= driver.find_element_by_class_name('_3u328' )
text_box.send_keys('Hello'+Keys.ENTER)


    
    
'''x_arg='//span[contains(@title, '+'Himanish'+')]'
target=WebDriverWait(driver,600).until(EC.presence_of_element_located((By.XPATH,x_arg)))'''
