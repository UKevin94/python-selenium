import logging
import unittest

from selenium import webdriver

from pages.index_page import IndexPage
from pages.search_page import SearchPage


class TestPageObject(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_search_bar(self):
        index_page = IndexPage(self.driver)
        index_page.search_item("dress")
        search_page = SearchPage(self.driver)
        search_page.print_first_elem()
        logging.info(self.driver.title)
        logging.info(index_page.driver.title)

    def tearDown(self):
        self.driver.close()
