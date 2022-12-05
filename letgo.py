import pandas as pd
import numpy as np

from bs4 import BeautifulSoup

import requests as re
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException




link = "https://www.letgo.com/"


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options=options)

driver.get(link)
time.sleep(30)

product_name = "Iphone"

text = "Geçen Sellmify diye bir app indirdim . Böyle İlanı alıcılar veriyor şunu şunu istiyorum diye. Gecen girdim baya telefon falan isteyen vardı özellikle  iphone  falan söyliyim dedim. Oraya bakabilirsiniz satmak için. Umarım satarsınız."

search_button = driver.find_element(By.XPATH,value = '//*[@id="container"]/header/div/div/div[2]/div/div/div[2]/div/form/fieldset/div/input')

search_button.send_keys(product_name)
time.sleep(10)
enter_button = driver.find_element(By.XPATH,value = '//*[@id="container"]/header/div/div/div[2]/div/div/div[3]').click()
time.sleep(10)


find_product_number = 10

starter_product_number = 20

basarılı = 1

scroll_1 = 0
scroll_2 = 50


item_num = 22
num = 100

while True:

    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    more_product_button = driver.find_element(By.XPATH,value = f'//*[@id="container"]/main/div/div/section/div/div/div[4]/div[2]/div/div[2]/ul/li[{item_num}]/div/button').click()

    item_num += 20
    
    # Wait to load page
    time.sleep(3)
    
    if item_num > num:
        break

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    
driver.find_element(By.TAG_NAME,value='body').send_keys(Keys.CONTROL + Keys.HOME)


for item in range(1,30):
    if item == 7:
        continue
    else:
        try:       
            driver.execute_script(f"window.scrollTo({scroll_1},{scroll_2})")
            scroll_1 += scroll_2
            scroll_2 += scroll_2
            value = f'//*[@id="container"]/main/div/div/section/div/div/div[4]/div[2]/div/div[2]/ul/li[{item}]/a'
            time.sleep(3)
            find_link = driver.find_element(By.XPATH,value = value).click()
            time.sleep(5)
            satıcıyla_sohbet_et = driver.find_element(By.XPATH,value = '//*[@id="container"]/main/div/div/div/div[5]/div[2]/div/div/button').click()
            time.sleep(5)
            try:
                continue_button = driver.find_element(By.XPATH,value = '//*[@id="container"]/main/div/div/div/div[6]/div[2]/div[2]/button').click()
                time.sleep(5) 
            except NoSuchElementException:
                print('Continue Button yok')
                                             
            button = driver.find_element(By.XPATH,value = '//*[@id="myDiv"]/div[2]/div/div[3]/div/div[2]/div/div[2]/textarea') 
            button.send_keys(text)
            time.sleep(5)
    
            # time.sleep(5)          
            send_text_button = driver.find_element(By.XPATH,value = '//*[@id="myDiv"]/div[2]/div/div[3]/div/div[2]/div/div[2]/span').click()
            time.sleep(5)
            basarılı += 1
            print(f"----- {item} ------")
            driver.back()
            time.sleep(5)
            driver.back()
            time.sleep(5)
    
        except NoSuchElementException:
            driver.back()
            time.sleep(5)
        


# ########################
# import pandas as pd
# import numpy as np

# from bs4 import BeautifulSoup

# import requests as re
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
# from selenium.common.exceptions import NoSuchElementException




# link = "https://www.letgo.com/maltepe_g5000442/q-Iphone-11?isSearchCall=true"


# options = webdriver.ChromeOptions()
# options.add_argument("--start-maximized")
# driver = webdriver.Chrome(chrome_options=options)

# driver.get(link)


# time.sleep(3)
# SCROLL_PAUSE_TIME = 1

# # Get scroll height
# last_height = driver.execute_script("return document.body.scrollHeight")

# check_products_number = driver.find_elements(By.CLASS_NAME,value = 'kPraq')
