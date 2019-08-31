#program for downloading makaut results

#for generating exe : pyinstaller --F -i "icon-path" makaut.py

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import  By

from selenium.webdriver.support.ui import Select#for taking action on finded element 
from selenium.webdriver.chrome.options import Options

#disabling the chrome pdf viewer so that pdf directly downloaded

print('All rights reserved with : JINDAL TECH. SOLS. PVT. LTD.')
print('AUTHOR : Karan Agarwal\n')
print("HELLO !!!")
print('Enter the range of roll numbers to get results for.')
print('Enter  the rolls ---A--- to ---B---')
print('\nA =',end='')
a=int(input())
print('\nB =',end='')
b=int(input())
print('\nEnter sem 1/2/3..... :',end='')
c=input()
print('\nResult is stored in the C drive in folder MakautResults')
print('In the path-C:\\MakautResults \n')

chrome_options = Options()
chrome_options.add_experimental_option('prefs',  {
    "download.default_directory": 'C:\\MakautResults',
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True
    }
)
driver= webdriver.Chrome(options = chrome_options)

for i in range(a,b+1):
    driver.get('https://makaut.ucanapply.com/smartexam/public/result-details')
    roll_box=driver.find_element_by_id('username')
    roll_box.send_keys(str(i))
    dropdown=Select(driver.find_element_by_id('semester'))
    dropdown.select_by_value('SM0'+c)
    go=driver.find_element_by_class_name('btn')
    go.click()
    pdf=driver.find_element_by_name('download-pdf-result')
    download=driver.find_element_by_class_name('btn-lg')
    download.submit()#since the button is of type submit

#switching tabs
#driver.switch_to.window(driver.window_handles[1])


