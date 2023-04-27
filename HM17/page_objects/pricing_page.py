from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from HM17.utilities.web_ui.base_page import BasePage


class Pricing(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__wait = WebDriverWait(self.driver, 10, 5)

    __tab_checker = (By.XPATH, "//div[@class='pricing__tabs__item pricing__tabs__item__checker']")
    __lifetime_radiobutton = (By.XPATH, "//label[@class='product__tariff__radio--label product__tariff__radio--label--holiday']")
    __button_buy_now = (By.XPATH, "//a[@class='NS-button auth_button NS-button__tangerine']")

    def click_checker_tab_button(self):
        self._click(self.__tab_checker)
        return self

    def click_buy_now_button(self):
        self._click(self.__button_buy_now)
        return self

    def click_lifetime_radiobutton(self):
        self._click(self.__lifetime_radiobutton)
        return self
