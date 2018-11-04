# import libraries


import http.cookiejar as cookielib
import os
import urllib
import re
import time
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import selenium
from bs4 import BeautifulSoup
import json


profil = {}
def scrap(browser):
    name = ""
    education = []
    profission =[]
    profil = {}

    soup = BeautifulSoup(browser.page_source, "html.parser")
    time.sleep(3)
    #name scrap
    browser.find_element_by_class_name('pv-top-card-section__name')
    Element = browser.find_element_by_class_name('pv-top-card-section__name')
    soup = BeautifulSoup(Element.get_attribute('innerHTML'), "html.parser")
    name = soup.get_text()
    profil['name']=name

    browser.execute_script("window.scrollBy(0,1000)")
    time.sleep(3)
    #experience section
    browser.implicitly_wait(10)
    Element = browser.find_element_by_id('experience-section')
    soup = BeautifulSoup(Element.get_attribute('innerHTML'), "html.parser")
    all_div = soup.find_all('li')
    for tag in all_div:
        company = {}
        time_work = []
        if tag.find(
            'span', {'class': 'pv-entity__secondary-title'}):
            company['name'] = tag.find(
                'span', {'class': 'pv-entity__secondary-title'}).get_text()
        if tag.find(
                'span', {'class': 'pv-entity__location'}):
            company['name'] = tag.find(
                'span', {'class': 'pv-entity__location'}).get_text()
        for el in tag.find_all('h4', {'class': 'pv-entity__date-range'}):
            for eli in el.find_all('span'):
                time_work.append(eli.get_text())
        company['time_work'] = time_work
        profission.append(company)
    profil["job"] = profission
    #education scrap
    Element = browser.find_element_by_id('education-section')
    soup = BeautifulSoup(Element.get_attribute('innerHTML'), "html.parser")
    # find all ul tag with specified class
    all_div = soup.find_all('li')
    for tag in all_div:
        ecole = {}
        time_study = []
        if tag.find(
                'h3', {'class': 'pv-entity__school-name'}):
            ecole['name'] = tag.find(
                'h3', {'class': 'pv-entity__school-name'}).get_text()
        for el in tag.find_all('time'):
            time_study.append(el.get_text())
        ecole['time_study'] = time_study
        education.append(ecole)
    #recomandation
    profil["education"] = education
    return profil
