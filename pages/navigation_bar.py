from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class NavigationBar(BasePage):

    _contact_link = (By.XPATH, "//div[@id='contact-link']/a")
    _search_bar = (By.XPATH, "//input[@id='search_query_top']")
    _search_bt = (By.XPATH, "//form[@id='searchbox']/button[@type='submit']")

    def __init__(self, driver):
        super().__init__(driver)

    def search_item(self, searched_str: str):
        self._type(self._search_bar, searched_str)
        self._click(self._search_bt)
