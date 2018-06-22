#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 11:06:43 2018

@author: prasunsarkar
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys

driver = webdriver.Chrome('/Users/prasunsarkar/Downloads/chromedrivers')

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

i = 0
colors =['"Hi hello 😅"','"Shreet"']

#colors = data[0]
#string = sys.argv[1]
for color in colors: 
  print(color)
  string = "Welcome to Milmila Tech India Pvt ! We will get back  to you very soon"
  x_arg = '//span[contains(@title,' + color + ')]'
  group_title = wait.until(EC.presence_of_element_located((
	By.XPATH, x_arg)))
  group_title.click()

  message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]

  message.send_keys(string)

  sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/button')[0]
  sendbutton.click()

db.close() 
driver.close()  