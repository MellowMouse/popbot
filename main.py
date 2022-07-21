from jokes import joke_list
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#setting driver to firefox and going to nate's site
#PATH = "users/chrisaraujo/desktop/popbot/chromedriver.exe"
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
elem.send_keys("picardlover69@hotmail.com")

#enter the joke into the message field and submit
elem = driver.find_element(By.ID, "form-field-message")
elem.clear()
elem.send_keys("Call 1 (888) 354-1369 for a chance to win a free cruise! Hurry before this offer run out!")
elem.send_keys(Keys.RETURN)

#close my connection
driver.close()