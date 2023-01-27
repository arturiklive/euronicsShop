from pages.euronics_page import EuronicsPage
from pages.base_page import BasePage
from pages.products_listing_page import ListingPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
import time


class TestShopPage:

    def test_shop(self, driver):
        base_page = BasePage(driver, "https://euronics.lv")
        base_page.open()

        search_page = EuronicsPage(driver)
        search_page.click_if_cookies_button_visible()
        search_page.search_form_fill_and_proceed()

        listing_page = ListingPage(driver)
        listing_page.click_random_product()

        product_page = ProductPage(driver)
        expected_name = product_page.get_expected_product_name()
        expected_price = product_page.get_expected_product_price()
        print(expected_name)
        print(expected_price)
        product_page.add_to_cart()
        product_page.go_to_cart()

        cart_page = CartPage(driver)
        actual_name = cart_page.get_product_name_in_cart()
        actual_price = cart_page.get_product_price_in_cart()
        print(actual_name)
        print(actual_price)
        cart_page.delete_product_from_cart()

        time.sleep(5)
