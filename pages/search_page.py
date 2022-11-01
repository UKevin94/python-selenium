import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.navigation_bar import NavigationBar


class SearchPage(NavigationBar):
    _first_elem = (By.XPATH, "//ul[contains(@class,'product_list')]/li//a[@class='product_img_link']")
    _search_title = (By.XPATH, "//h1[contains(text(),'Search')]")

    def __init__(self, driver):
        super().__init__(driver)
        wait = WebDriverWait(driver, 10)
        wait.until(expected_conditions.visibility_of_element_located(self._search_title))

    def print_first_elem(self):
        logging.info(self._find(self._first_elem).get_property("title"))
