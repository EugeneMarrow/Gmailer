#coding: utf-8 
import re
import getpass
import pytest
from selenium import webdriver
from selenium import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import random
import string
import getpass

log = "username@gmail.com"
passw = "parolb"
@pytest.fixture(scope="session", autouse=True)
def driver():     
# Setup for remote driver,
    # Switch IP in command_executor to your host machine IP (ex: 192.168.0.1) if running from docker:
    # capabilities = {
    #     "browserName": "chrome",
    #     "version": "",
    #     "enableVNC": True,
    #     "enableVideo": False
    # }
    # driver = webdriver.Remote(
    #     command_executor="http://0.0.0.0:4444/wd/hub",
    #     desired_capabilities=capabilities)
# Setup for local chrome browser:
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def find(meth, val,driver):
    sleep(1)
    WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
            ( meth, val)
            ))
    return driver.find_element(meth, val)


@pytest.fixture(autouse=True)
def gmail_login(driver):
    driver.get("https://accounts.google.com/AccountChooser?service=mail&continue=https://mail.google.com/mail/")
    find(By.ID,"identifierId",driver).send_keys(log)
    find(By.ID,"identifierNext",driver).click()
    find(By.NAME,"password",driver).send_keys(passw)
    find(By.ID,"passwordNext",driver).click()
    sleep(4)
    assert(driver.current_url)=="https://mail.google.com/mail/u/0/#inbox"
    print "Succesfully logged in"

