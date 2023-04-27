from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from HM17.utilities.web_ui.base_page import BasePage


class ForgotPassword(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__wait = WebDriverWait(self.driver, 20, 10)


