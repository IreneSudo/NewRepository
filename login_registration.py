from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://demo.automationtesting.in/Register.html")
driver.implicitly_wait(5)
account_btn = driver.find_element(By.LINK_TEXT,"My Account")
account_btn.click()
Emadress = driver.find_element(By.ID, "username")
Emadress.send_keys("ira.sudilpovskaya@gmail.com")
password = driver.find_element(By.ID, "password")
password.send_keys("UkiHill53")
login_btn = driver.find_element(By.NAME"login")
login_btn.click()

driver.quit()
