from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://demo.automationtesting.in/Register.html")
driver.implicitly_wait(5)

account_btn = driver.find_element(By.LINK_TEXT,"My Account")
account_btn.click()
Emadress = driver.find_element(By.ID, "username")
Emadress.send_keys("ira.sudilpovskaya@gmail.com")
password = driver.find_element(By.ID, "password")
password.send_keys("UkiHill53%!!!&")
login_btn = driver.find_element(By.NAME,"login")
login_btn.click()

orderby = driver.find_element_by_name("orderby")
orderby_default = orderby.get_attribute("value")
if orderby_default == "menu_order":
    print("Выбрана сортировка по умолчанию")
else:
    print("Выбрана другая сортировка")


orderby = driver.find_element(By.NAME,"orderby")
select = Select(orderby)
select.select_by_value("price-desc")
orderby_us = orderby.get_attribute("value")
if orderby_us == "price-desc": # если равно какому-либо значению
    print ("Товары отсортированы по убыванию")
else:
    print ("Нужная сортировка не выбрана")

driver.quit()


driver.quit()

