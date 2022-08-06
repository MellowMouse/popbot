from multiprocessing.connection import wait
from emails import emails
from jokes import joke_list
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random
import time



#getting random joke
num = random.randint(0,59)
joke = joke_list[num]

#getting a random email
rand_email = random.randint(0,9)
email = emails[rand_email]

#setting driver to firefox and going to nate's site
PATH = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("https://apexsoccer.org")

#enter eric jones into nate's "Name" field of his user form
elem = driver.find_element(By.ID, "form-field-name")
elem.clear()
elem.send_keys("Eric Jones")

#enter a ridiculous email into the "Email field"
second_elem = driver.find_element(By.ID, "form-field-email")
second_elem.clear()
second_elem.send_keys(email)

#enter the joke into the message field and submit
third_elem = driver.find_element(By.ID, "form-field-6ed25c0")
third_elem.clear()
third_elem.send_keys(joke)

click_elem = driver.find_element(By.TAG_NAME, "button")
click_elem.click()

time.sleep(3)
#close my connection
driver.close()