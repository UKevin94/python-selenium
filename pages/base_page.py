from selenium import webdriver


class BasePage:
    def __init__(self, driver: webdriver):
        self.driver = driver

    def _visit(self, url: str):
        self.driver.get(url)

    def _find(self, locator: tuple):
        return self.driver.find_element(locator[0], locator[1])

    def _click(self, locator: tuple):
        self._find(locator).click()

    def _type(self, locator: tuple, input_text: str):
        self._find(locator).send_keys(input_text)
