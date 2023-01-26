from pages.base_page import BasePage
from locators.page_locators import PageLocators as Locators


class ProductPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def get_expected_product_name(self):
        return self.element_is_visible(Locators.EXPECTED_PRODUCT_NAME_PRODUCT_PAGE)

    def get_expected_product_price(self):
        return self.element_is_visible(Locators.EXPECTED_PRODUCT_PRICE_PRODUCT_PAGE).get_attribute('textContent')

    def add_to_cart(self):
        self.element_is_visible(Locators.ADD_TO_CART).click()

    def go_to_cart(self):
        self.element_is_visible(Locators.GO_TO_CART_BUTTON).click()