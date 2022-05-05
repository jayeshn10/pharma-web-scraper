import pandas as pd
import requests
from bs4 import BeautifulSoup

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get('https://www.1mg.com/drugs-therapeutic-classes')


elem = browser.find_element(By.CLASS_NAME, 'style__category-list___wPLNO')


cat_div = elem.find_elements(By.CLASS_NAME,'style__category___3TRar')

dict = {'category': [],
        'sub-category': [],
        'category url': []
        }

df = pd.DataFrame(dict)


for c in cat_div:
    c.click()
    subcat_list = browser.find_elements(By.XPATH,"//div[contains(@class, 'style__active___3gtoG')]/div/div")
    #print(subcat)
    #subcat_list = subcat.find_elements(By.CLASS_NAME,'style__sub-category___2354n')
    for sc in subcat_list:

        a = sc.find_element(By.TAG_NAME,"a")
        print(c.text,"category")
        print(sc.text,"---sub category")
        print(a.get_attribute("href"),"---a")

        df2 = {'category':c.text, 'sub-category': sc.text, 'category url': a.get_attribute("href")}
        df = df.append(df2,ignore_index=True)



df.to_csv('med_cat.csv')



browser.quit()
