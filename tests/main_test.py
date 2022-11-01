import time

import pytest
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from pages.index_page import IndexPage
from pages.search_page import SearchPage


# put this to fixture ?
def logging_configuration():
    logging.basicConfig(level=logging.INFO)


def test_first():
    logging_configuration()
    logging.info("This is only the start")
    logging.debug("I'm bored as fk")
    logging.warning("This is a warning")


@pytest.mark.skip
def test_skip():
    logging_configuration()
    logging.warning("This should be skipped")


@pytest.mark.skipif(3 > 2, reason="this will never work")
def test_skip_cond():
    logging_configuration()
    logging.warning("This should be skipped depending on condition")


@pytest.mark.xfail
def test_fail():
    assert 1 > 2


@pytest.mark.skip
@pytest.mark.parametrize("a,b", [(1, 2), (3, 1), (5, 8)])
def test_parameterized(a: int, b: int):
    assert a > b


@pytest.mark.skip
def test_selenium():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get('https://www.python.org')
    assert driver.current_url == 'https://www.python.org/', "zzzz"
    assert driver.title == 'Welcome to Python.org', 'zzzzzzzzzz'
    driver.quit()


@pytest.mark.skip
def test_multiple_browser():
    logging_configuration()
    logging.basicConfig(level=logging.INFO)
    driver1 = webdriver.Firefox()
    driver1.get("https://www.python.org")
    driver2 = webdriver.Firefox()
    driver2.get("https://ruby-lang.org")
    logging.info(driver1.title)
    logging.info(driver2.title)
    driver1.quit()
    driver2.quit()


@pytest.mark.skip
def test_iframe():
    driver = webdriver.Firefox()
    driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert")
    driver.find_element(By.XPATH, "//div[@id='accept-choices']").click()
    right_frame = driver.find_element(By.XPATH, "//iframe[@id='iframeResult']")
    driver.switch_to.frame(right_frame)
    try_bt = driver.find_element(By.XPATH, "//button[text()='Try it']")
    driver.switch_to.default_content()
    main_div = driver.find_element(By.XPATH, "//div[@id='tryitLeaderboard']")


@pytest.mark.skip
def test_selenium_screenshot():
    driver1 = webdriver.Firefox()
    driver1.get("https://www.python.org")
    driver2 = webdriver.Firefox()
    driver2.get("https://ruby-lang.org")
    driver1.maximize_window()
    driver2.maximize_window()
    driver1.get_screenshot_as_file('python_sc.png')
    driver2.get_screenshot_as_file('ruby_sc.png')
    driver1.quit()
    driver2.quit()


@pytest.mark.skip
def test_get_element():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get('http://automationpractice.com/index.php')
    search_bar = driver.find_element(By.ID, "search_query_top")
    logging.info(search_bar.get_property("name"))
    sign_in_bt = driver.find_element(By.CLASS_NAME, "login")
    logging.info(sign_in_bt.get_property("title"))
    header_1 = driver.find_element(By.TAG_NAME, "h1")
    logging.info(header_1.text)
    contact_txt = driver.find_element(By.LINK_TEXT, "Contact us")
    logging.info(contact_txt.get_property("title"))
    img_css = driver.find_element(By.CSS_SELECTOR, "a[title='My Store'] > img")
    logging.info(img_css.get_property("src"))
    driver.quit()


@pytest.mark.skip
def test_check_attribute():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get('http://automationpractice.com/index.php?id_category=8&controller=category#/')
    casu_cb = driver.find_element(By.ID, "layered_category_9")
    logging.info(casu_cb.is_selected())
    casu_cb.click()
    logging.info(casu_cb.is_selected())
    search_bar = driver.find_element(By.ID, "search_query_top")
    search_bar.send_keys("toto")
    logging.info(search_bar.get_property("value"))
    search_bar.clear()
    logging.info("latest value : " + search_bar.get_property("value"))
    driver.quit()


@pytest.mark.skip
def test_select_sort():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get('http://automationpractice.com/index.php?id_category=8&controller=category#/')
    select_sort = Select(driver.find_element(By.ID, "selectProductSort"))
    select_sort.select_by_index(2)
    logging.info(select_sort.first_selected_option.text)
    select_sort.select_by_visible_text("In stock")
    logging.info(select_sort.first_selected_option.text)
    select_sort.select_by_value("name:asc")
    logging.info(select_sort.first_selected_option.text)
    driver.quit()


@pytest.mark.skip
def test_modal():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 10)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get('http://automationpractice.com')
    prod_img = driver.find_element(By.XPATH, "//a[@title='Faded Short Sleeve T-shirts']")
    driver.execute_script("arguments[0].scrollIntoView();", prod_img)
    actions = ActionChains(driver)
    actions.move_to_element(prod_img).perform()
    prod_link = driver.find_element(By.XPATH, "//a[@title='Faded Short Sleeve T-shirts']/../a[@class='quick-view']")
    #driver.execute_script("arguments[0].scrollIntoView();", prod_link)
    prod_link.click()
    item_iframe = driver.find_element(By.XPATH, "//iframe[@class='fancybox-iframe']")
    wait.until(expected_conditions.visibility_of(item_iframe))
    driver.switch_to.frame(item_iframe)
    add_to_cart_bt = driver.find_element(By.XPATH, "//p[@id='add_to_cart']")
    add_to_cart_bt.click()
    driver.switch_to.default_content()
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//i[@class='icon-ok']")))
    added_txt = driver.find_element(By.XPATH, "//h2")
    logging.info(added_txt.text)
    driver.quit()


@pytest.mark.skip
def test_alert():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 10)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get('https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert')
    driver.find_element(By.XPATH, "//div[@id='accept-choices']").click()
    right_frame = driver.find_element(By.XPATH, "//iframe[@id='iframeResult']")
    driver.switch_to.frame(right_frame)
    try_bt = driver.find_element(By.XPATH, "//button[text()='Try it']")
    try_bt.click()
    alert = driver.switch_to.alert
    logging.info(alert.text)
    alert.accept()
    driver.quit()


@pytest.mark.skip
def test_wait_search():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 10)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get('http://automationpractice.com/index.php')
    search_input = driver.find_element(By.XPATH, "//input[@id='search_query_top']")
    search_input.send_keys("dress")
    driver.find_element(By.XPATH, "//button[@name='submit_search']").click()
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Search')]/span[contains(text(),'dress')]")))
    first_elem = driver.find_element(By.XPATH, "//a[@title='Printed Summer Dress']")
    logging.info(first_elem.get_property("href"))
    driver.quit()


@pytest.mark.skip
def test_page_object():
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.maximize_window()
    index_page = IndexPage(driver)
    index_page.search_item("dress")
    search_page = SearchPage(driver)
    search_page.print_first_elem()
    logging.info(driver.title)
    logging.info(index_page.driver.title)
