
import selenium
from pages.base_page import BasePage
from locators.page_locators import PageLocators as Locators
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
class ProductPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def get_expected_product_name(self):
        self.element_is_visible(Locators.ACTUAL_PRODUCT_NAME_PRODUCT_PAGE)

    def get_expected_product_price(self):
        self.element_is_visible(Locators.ACTUAL_PRODUCT_PRICE_PRODUCT_PAGE)

    def add_to_cart(self):
        self.element_is_visible(Locators.ADD_TO_CART).click()