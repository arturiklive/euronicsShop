from pages.base_page import BasePage
from locators.page_locators import PageLocators as Locators


class CartPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def get_product_name_in_cart(self):
        return self.element_is_visible(Locators.ACTUAL_PRODUCT_NAME_CART).text.split()

    def get_product_price_in_cart(self):
        return self.element_is_visible(Locators.ACTUAL_PRODUCT_PRICE_CART).text.split().replace("€", "")

    def delete_product_from_cart(self):
        self.element_is_visible(Locators.DELETE_PRODUCT_FROM_CART).click()
