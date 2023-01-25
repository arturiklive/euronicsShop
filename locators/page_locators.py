from selenium.webdriver.common.by import By
from random import randint
class PageLocators:
    COOKIES_ACCEPT_BUTTON = (By.ID, "cookie-accept-all-button")
    SEARCH_TEXTFORM = (By.XPATH, "//input[@class='autocomplete__input']")
    SEARCH_DO_BUTTON = (By.XPATH, "//i[@class=' far fa-search']")
    SEARCH_RESULT_HEADER = (By.XPATH, "//h1[@class='category__header']")
    RANDOM_PRODUCT_LINK = (By.XPATH, f"(//span[@class='product-card__title'])[{randint(1,6)}]")
    ACTUAL_PRODUCT_NAME_PRODUCT_PAGE = (By.XPATH, "(//h1[@class='product__title'])[2]")
    ACTUAL_PRODUCT_PRICE_PRODUCT_PAGE = (By.XPATH,  "//span[@class='price__original']")
    ADD_TO_CART = (By.XPATH,  "//button[@data-add-to-cart-id]")