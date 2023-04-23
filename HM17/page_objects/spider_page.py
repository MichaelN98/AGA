from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Spider:
    def __init__(self, driver):
        self.driver = driver
        self.__wait = WebDriverWait(self.driver, 20, 10)

    __h1_spider_page = (
        By.XPATH, "//h1[contains(text(),'The desktop tool for everyday SEO audits')]")

    def is_spider_page_displayed(self):
        is_spider_page_element = self.__wait.until(EC.visibility_of_element_located(self.__h1_spider_page))
        return is_spider_page_element.is_displayed()
