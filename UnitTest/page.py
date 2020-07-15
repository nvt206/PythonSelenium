from locator import *
from element import BasePageElement


class SearchTextElement(BasePageElement):
    # locator = "q"
    def __init__(self, locator):
        self.locator = locator


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    search_text_element = SearchTextElement("#id-search-field")
    def is_title_matches(self):
        return "Python" in self.driver.title

    def click_go_button(self):
        element = self.driver.find_element(*MainBaseLocators().GO_BUTTON)
        element.click()


class SearchResultPage(BasePage):

    def is_result_found(self):
        return "No results found." not in self.driver.page_source
