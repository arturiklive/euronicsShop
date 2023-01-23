import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()

searchText = "apple m1"
linkSearchField = "//input[@class='autocomplete__input']"
linkSearchFieldGo = "//i[@class=' far fa-search']"
linkSearchResult = "//h1"

driver.get("https://www.euronics.lv/")
driver.find_element("xpath", linkSearchField).send_keys(searchText)
driver.find_element("xpath", linkSearchFieldGo).click()

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, linkSearchResult)))
searchResultText = driver.find_element("xpath", linkSearchResult).text
print(searchText)
print(searchResultText)

assert searchResultText in searchText

time.sleep(5)
driver.close()
driver.quit()
