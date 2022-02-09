from selenium import webdriver
from config import username, pass_word
title = "NITK Captive Portal"

url = "https://nac.nitk.ac.in:8090"

driver = webdriver.Chrome()
driver.get(url)

assert title in driver.title
user_name = driver.find_element_by_id("username")
user_name.clear()
user_name.send_keys(username)

password = driver.find_element_by_id("password")
password.clear()
password.send_keys(pass_word)

signin_btn = driver.find_element_by_id("loginbutton")
signin_btn.click()

driver.close()