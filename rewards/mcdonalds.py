#!/usr/bin/python
import os, sys, random, time, datetime
from unidecode import unidecode
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# vaiables
survey_code = "37102128402211815374000108"

# open chrome and set explicit wait time
driver = webdriver.Chrome()
wait = WebDriverWait(driver,5)

# go to mc donalds reciept survey
driver.get('www.mcdvoice.com')

# enter survey code: 37102128402211815374000108
element = wait.until(EC.presence_of_element_located((By.XPATH, "//span/input[@id='CN1']")))
for s in survey_code:
	element.send_keys(s)
element = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='NextButton']")))
element.click()

# take survey


# get message to return
element = wait.until(EC.presence_of_element_located((By.XPATH, "//p[@class='ValCode']")))
print element.text