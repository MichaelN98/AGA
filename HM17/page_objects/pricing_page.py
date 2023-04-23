from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from HM17.utilities.web_ui.base_page import BasePage


class Pricing(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__wait = WebDriverWait(self.driver, 10, 5)

    __plans_and_pricing = (By.XPATH, "//div[contains(text(),'Plans & Pricing')]")
    __tab_checker = (By.XPATH, "//div[@class='pricing__tabs__item pricing__tabs__item__checker']")
    __is_tab_checker = (By.XPATH, "//div[@class='pricing__tabs__item pricing__tabs__item__checker active']")

    __lifetime_radiobutton = (By.XPATH, "//label[@class='product__tariff__radio--label product__tariff__radio--label--holiday']")
    __is_lifetime_tariffs = (By.XPATH, "//div[@class='plan_card__description plan_card__description_price']")

    __button_buy_now = (By.XPATH, "//a[@class='NS-button auth_button NS-button__tangerine']")

    def is_pricing_displayed(self):
        plans_and_pricing_element = self.__wait.until(EC.visibility_of_element_located(self.__plans_and_pricing))
        return plans_and_pricing_element.is_displayed()

    def click_checker_tab_button(self):
        self._click(self.__tab_checker)
        return self

    def is_checker_tab_displayed(self):
        checker_tab_element = self.__wait.until(EC.visibility_of_element_located(self.__is_tab_checker))
        return checker_tab_element.is_displayed()

    def click_lifetime_radiobutton(self):
        self._click(self.__lifetime_radiobutton)
        return self

    def is_lifetime_displayed(self):
        lifetime_element = self.__wait.until(EC.visibility_of_element_located(self.__is_lifetime_tariffs))
        return lifetime_element.is_displayed()

    def click_buy_now_button(self):
        self._click(self.__button_buy_now)
        return self
