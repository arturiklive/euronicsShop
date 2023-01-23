import time
import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()

search_text = "apple m1"
driver.get("https://www.euronics.lv/")

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "cookie-accept-all-button")))
if (driver.find_element(By.ID, "cookie-accept-all-button")):
    driver.find_element(By.ID, "cookie-accept-all-button").click()

driver.find_element("xpath", "//input[@class='autocomplete__input']").send_keys(search_text)
driver.find_element("xpath", "//i[@class=' far fa-search']").click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1[@class='category__header']")))

search_result_text = driver.find_element("xpath", "//h1[@class='category__header']").text

assert search_result_text in search_text

random_product_number = random.randint(1,10)
print(random_product_number)
driver.find_element("xpath", "(//span[@class='product-card__title'])["+str(random_product_number)+"]").click()

time.sleep(5)
driver.close()
driver.quit()
