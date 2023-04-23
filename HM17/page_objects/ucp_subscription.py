from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UcpSubscription:
    def __init__(self, driver):
        self.driver = driver
        self.__wait = WebDriverWait(self.driver, 15, 5)

    __h1_subscription = (By.XPATH, "//h1[@class='header__title']")

    def is_h1_subscription_displayed(self):
        h1_subscription_element = self.__wait.until(EC.visibility_of_element_located(self.__h1_subscription))
        return h1_subscription_element.is_displayed()
