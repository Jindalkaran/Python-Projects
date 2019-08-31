from selenium import webdriver
browser=webdriver.Chrome("C:/Users/karan/Documents/Pythons/NEPPTEL/chromedriver")
browser.get("https:\\www.facebook.com")


search=browser.find_element_by_id('email')
search.send_keys('yashagarwalgms@yahoo.com')
search=browser.find_element_by_id('pass')
search.send_keys('9832490338')

login=browser.find_element_by_id("loginbutton")
login.click()
