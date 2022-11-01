from pages.navigation_bar import NavigationBar


class IndexPage(NavigationBar):
    def __init__(self, driver):
        super().__init__(driver)
        self._visit("http://automationpractice.com/index.php")
