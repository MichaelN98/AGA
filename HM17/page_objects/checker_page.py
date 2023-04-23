from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Checker:
    def __init__(self, driver):
        self.driver = driver
        self.__wait = WebDriverWait(self.driver, 20, 10)

    __h1_checker_page = (
        By.XPATH, "//h1[contains(text(),'Compare your websites in bulk with SERP scraping')]")

    def is_checker_page_displayed(self):
        is_checker_page_element = self.__wait.until(EC.visibility_of_element_located(self.__h1_checker_page))
        return is_checker_page_element.is_displayed()
