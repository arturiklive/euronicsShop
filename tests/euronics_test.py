from pages.euronics_page import EuronicsPage
from pages.base_page import BasePage
from pages.products_listing_page import ListingPage
from pages.product_page import ProductPage
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
        product_page.add_to_cart()

        time.sleep(5)