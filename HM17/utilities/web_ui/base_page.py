from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.__wait = WebDriverWait(self.driver, 15, 1)

    __h1_checker_page = (
        By.XPATH, "//h1[contains(text(),'Compare your websites in bulk with SERP scraping')]")

    __h1_forgot_password_page = (
        By.XPATH, "//span[contains(text(),'To reset the password, enter the email you used to')]")
    __error_message = (By.XPATH, "//span[contains(text(),'Invalid email or password entered')]")
    __show_input_password = (By.XPATH, "//input[@type='text']")
    __is_open_multisearch = (By.XPATH, "//input[@id='q']")
    __h1_sign_up_page = (
        By.XPATH, "//h1[contains(text(),'Great SEO starts with an account')]")
    __h1_spider_page = (
        By.XPATH, "//h1[contains(text(),'The desktop tool for everyday SEO audits')]")
    __h1_licenses = (By.XPATH, "//h1[@class='licenses__heading']")
    __h1_subscription = (By.XPATH, "//h1[@class='header__title']")
    __main_page = (By.XPATH, "//h1[contains(text(),'Easy-to-use & robust SEO analytics for all')]")
    __2_badges = (By.XPATH, "//div[@class='home-page__head__left__bages home-page__head__left__bages__notLogin en']")
    __popup_register = (By.XPATH, "//h1[contains(text(),'Great SEO starts with an account')]")
    __open_dropdown_products = (By.XPATH, "//div[@class='dropdown-menu header-dropdown-menu p-y-0']")
    __pop_up_login = (By.XPATH, "//h1[contains(text(),'Log in to your account')]")
    __plans_and_pricing = (By.XPATH, "//div[contains(text(),'Plans & Pricing')]")
    __is_tab_checker = (By.XPATH, "//div[@class='pricing__tabs__item pricing__tabs__item__checker active']")
    __is_lifetime_tariffs = (By.XPATH, "//div[@class='plan_card__description plan_card__description_price']")

    def is_checker_tab_displayed(self):
        checker_tab_element = self.__wait.until(EC.visibility_of_element_located(self.__is_tab_checker))
        return checker_tab_element.is_displayed()

    def is_lifetime_displayed(self):
        lifetime_element = self.__wait.until(EC.visibility_of_element_located(self.__is_lifetime_tariffs))
        return lifetime_element.is_displayed()

    def is_pricing_displayed(self):
        plans_and_pricing_element = self.__wait.until(EC.visibility_of_element_located(self.__plans_and_pricing))
        return plans_and_pricing_element.is_displayed()

    def is_popup_login_displayed(self):
        popup_login_element = self.__wait.until(EC.visibility_of_element_located(self.__pop_up_login))
        return popup_login_element.is_displayed()

    def is_open_dropdowm_header(self):
        dropdown_element = self.__wait.until(EC.visibility_of_element_located(self.__open_dropdown_products))
        return dropdown_element.is_displayed()

    def is_popup_register_displayed(self):
        popup_register_element = self.__wait.until(EC.visibility_of_element_located(self.__popup_register))
        return popup_register_element.is_displayed()

    def is_h1_main_page_displayed(self):
        h1_main_page_element = self.__wait.until(EC.visibility_of_element_located(self.__main_page))
        return h1_main_page_element.is_displayed()

    def is_2badges_main_page_displayed(self):
        badges_main_page_element = self.__wait.until(EC.visibility_of_element_located(self.__2_badges))
        return badges_main_page_element.is_displayed()

    def is_h1_subscription_displayed(self):
        h1_subscription_element = self.__wait.until(EC.visibility_of_element_located(self.__h1_subscription))
        return h1_subscription_element.is_displayed()

    def is_h1_licenses_displayed(self):
        h1_licenses_element = self.__wait.until(EC.visibility_of_element_located(self.__h1_licenses))
        return h1_licenses_element.is_displayed()

    def is_spider_page_displayed(self):
        is_spider_page_element = self.__wait.until(EC.visibility_of_element_located(self.__h1_spider_page))
        return is_spider_page_element.is_displayed()

    def is_sign_up_displayed(self):
        is_sign_up_element = self.__wait.until(EC.visibility_of_element_located(self.__h1_sign_up_page))
        return is_sign_up_element.is_displayed()

    def is_show_password(self):
        show_password_element = self.__wait.until(EC.visibility_of_element_located(self.__show_input_password))
        return show_password_element.is_displayed()

    def is_open_multisearch(self):
        open_multisearch_element = self.__wait.until(EC.visibility_of_element_located(self.__is_open_multisearch))
        return open_multisearch_element.is_displayed()

    def is_error_message_displayed(self):
        error_message_element = self.__wait.until(EC.visibility_of_element_located(self.__error_message))
        return error_message_element.is_displayed()

    def is_forgot_password_dispayed(self):
        is_forgot_password_element = self.__wait.until(EC.visibility_of_element_located(self.__h1_forgot_password_page))
        return is_forgot_password_element.is_displayed()

    def is_checker_page_displayed(self):
        is_checker_page_element = self.__wait.until(EC.visibility_of_element_located(self.__h1_checker_page))
        return is_checker_page_element.is_displayed()

    def _wait_until_element_located(self, locator):
        return self.__wait.until(EC.presence_of_element_located(locator))

    def _wait_until_to_be_clickable(self, locator):
        return self.__wait.until(EC.element_to_be_clickable(locator))

    def _wait_until_element_visible(self, locator):
        return self.__wait.until(EC.visibility_of_element_located(locator))

    def _send_keys(self, locator, value, is_clear=True):
        element = self._wait_until_element_located(locator)
        if is_clear:
            element.clear()
        element.send_keys(value)

    def _click(self, locator):
        self._wait_until_to_be_clickable(locator).click()


