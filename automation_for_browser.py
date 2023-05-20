#!/usr/bin/env python
# coding: utf-8

# # Chrome Driver
# ### Download the chrome driver
# ### https://chromedriver.chromium.org/


website = "https://"
page = f"{website}/residences.html?city=26"

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import os
import random

driver = None


def start():
    global driver
    service = Service(executable_path="chromedriver_mac64/chromedriver")
    driver = webdriver.Chrome(service=service)
    driver.get(page)

def click_filter():
    elem = driver.find_element(By.XPATH, "/html/body/div[3]/main/div[2]/div/section/div/div[2]/div[1]/div[3]/div/div[3]/div/div[1]/div[1]")
    elem.click()


def click_book():
    ref = "/html/body/div[3]/main/div[2]/div/section/div/div[2]/div[1]/div[3]/div/div[3]/div/div[1]/div[2]/ol/li[1]/input"
    elem  = driver.find_element(By.XPATH, ref)
    elem.click()

def get_block_source():
    reg = "/html/body/div[3]/main/div[2]/div/section/div/div[2]/div[2]/div[2]/div[1]/div"
    return driver.find_element(By.XPATH, reg).text

def alarm():
    for _ in range(500):
        os.system('afplay /System/Library/Sounds/Submarine.aiff -v 10')



snapshot_prev = None
snapshot = None
flag = True
while True:
    start()
    sleep(5)
    source = driver.page_source

    sleep(10)
    while True:
        try:
            source = driver.page_source
            if "Available to book" in source:
                try:
                    is_checked = driver.find_element(By.XPATH,"/html/body/div[3]/main/div[2]/div/section/div/div[2]/div[1]/div[3]/div/div[3]/div[3]/div[1]/div[2]/ol/li[1]/input").get_attribute("checked")
                except:
                    is_checked = "false"
                    
                if is_checked != "true":
                    click_book()
                    sleep(5)
                snapshot = get_block_source()
                if flag:
                    snapshot_prev = snapshot
                    flag = False
            
            if snapshot != snapshot_prev:
                alarm()
                sleep(600)

            sleep(random.randint(5,15))
            driver.refresh()
        except Exception as e:
            print(e)
            driver.close()
            break
