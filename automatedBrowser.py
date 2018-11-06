
import http.cookiejar as cookielib
import os
import urllib
import re
import time
from Scraper import scrap
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import selenium
from bs4 import BeautifulSoup
import json
from random import randint
import user


browser = webdriver.Chrome()



cookie_filename = "parser.cookies.txt"
profils={}


browser.get('https://www.linkedin.com/')
elem = browser.find_element_by_id('login-email')
elem.send_keys(user.GetUserName() + Keys.RETURN)
elem2 = browser.find_element_by_id('login-password')
elem2.send_keys(user.GetUserPassword() + Keys.RETURN)
browser.implicitly_wait(10)
browser.find_element_by_class_name('profile-rail-card__actor-link').click()
count = 0
while count < 100:
    try:
        profils[count] = scrap(browser)
    except Exception:
        profils[count]=""
        pass
    #print(soup.prettify())
    browser.execute_script("window.scrollBy(0,-1000)")


    if count==0:
        browser.find_element_by_class_name(
            'pv-top-card-v2-section__link--connections').click()
        print('clicked')
    else:
        try:
            browser.find_element_by_class_name(
                'pv-highlight-entity__card-action-link').click()
        except Exception:
            print('noop')
            pass

    time.sleep(3)
    ulElemnt = browser.find_element_by_class_name(
        'search-results__list')
    numberR = str(randint(2, 7))
    
    browser.execute_script("window.scrollBy(0,300)")
    time.sleep(3)
    soup = BeautifulSoup(ulElemnt.find_element_by_xpath(
        "(.//*[@class='search-result__wrapper'])["+ numberR + "]").get_attribute('innerHTML'), "html.parser")
    ulElemnt.find_element_by_xpath(
        "(.//*[@class='search-result__image-wrapper'])["+ numberR +"]").click()
   
    print(count)
    count += 1
    with open('data.json', 'w', encoding='utf8') as outfile:
        json.dump(profils, outfile, sort_keys=True,indent=4, ensure_ascii=False)
yo = json.dumps(profils)
print(yo)
