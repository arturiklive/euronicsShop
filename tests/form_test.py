from pages.form_page import FormPage

class TestFormPage:

    def test_form(self, driver):
        form_page = FormPage(driver, "https://euronics.lv")
        form_page.open()