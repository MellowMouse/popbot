from emails import emails
from jokes import joke_list
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random

#getting random joke
num = random.randint(0,59)
joke =joke_list[num]

#getting a random email
rand_email = random.randint(0,9)
email = emails[rand_email]

#setting driver to firefox and going to nate's site
PATH = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("https://apexsoccer.org/pods/")

#enter eric jones into nate's "Name" field of his user form
elem = driver.find_element(By.ID, "form-field-name")
elem.clear()
elem.send_keys("Eric Jones")

#enter a ridiculous email into the "Email field"
elem = driver.find_element(By.ID, "form-field-email")
elem.clear()
elem.send_keys(email)

#enter the joke into the message field and submit
elem = driver.find_element(By.ID, "form-field-message")
elem.clear()
elem.send_keys(joke)
elem.send_keys(Keys.RETURN)

#close my connection
driver.close()