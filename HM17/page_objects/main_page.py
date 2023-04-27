from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from HM17.page_objects.checker_page import Checker
from HM17.page_objects.pricing_page import Pricing
from HM17.page_objects.spider_page import Spider
from HM17.utilities.web_ui.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__wait = WebDriverWait(self.driver, 20, 10)

    __free_download_button = (
        By.XPATH, "//a[@id='try_it_for_free_first' and @class='auth_button NS-button NS-button__greenblueClear']")

    __buy_now_button = (By.XPATH, "//a[@class='NS-button NS-button__tangerine NS-button__gift']")

    __pricing_head = (By.XPATH, "//body/div[5]/div[1]/nav[1]/div[2]/div[2]/ul[1]/li[2]/a[1]")
    __close_banner = (By.XPATH, "//span[@class='NS-popUp__close js-closePopUp']")
    __close_popoup_register = (By.XPATH, "//span[@class='NS-modal__close']")

    __products_head = (By.XPATH, "//li[@class='dropdown']")
    __products_head_spider = (By.XPATH, "//p[contains(text(),'Your personal SEO crawler')]")
    __products_head_checker = (By.XPATH, "//p[contains(text(),'Research tool for bulk SEO analysis')]")
    __free_download_button_in_header = (
        By.XPATH,
        "//a[@class='auth_button btn btn-discount btn-discount--success NS-button NS-button__greenblueClear header__login_btn']")

    __login_header = (By.XPATH, "//a[@class='auth_button']")

    __open_dropdown_products = (By.XPATH, "//div[@class='dropdown-menu header-dropdown-menu p-y-0']")

    def click_free_download_button(self):
        self._click(self.__free_download_button)
        return self

    def click_close_popup_button(self):
        self._click(self.__close_popoup_register)
        return MainPage(self.driver)

    def click_buy_now_button(self):
        self._click(self.__buy_now_button)
        return Pricing(self.driver)

    def click_pricing_head_button(self):
        self._click(self.__pricing_head)
        return Pricing(self.driver)

    def click_x_in_banner(self):
        self._click(self.__close_banner)
        return self

    def click_button_products(self):
        self._click(self.__products_head)
        return self

    def click_in_dropdown_products_spider_head(self):
        self._click(self.__products_head_spider)
        return Spider(self.driver)

    def click_in_dropdown_products_checker_head(self):
        self._click(self.__products_head_checker)
        return self

    def click_free_download_button_in_header(self):
        self._click(self.__free_download_button_in_header)
        return self

    def click_login_in_header(self):
        self._click(self.__login_header)
        return self


