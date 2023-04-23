from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UcpLicenses:
    def __init__(self, driver):
        self.driver = driver
        self.__wait = WebDriverWait(self.driver, 20, 10)

    __h1_licenses = (By.XPATH, "//h1[@class='licenses__heading']")

    def is_h1_licenses_displayed(self):
        h1_licenses_element = self.__wait.until(EC.visibility_of_element_located(self.__h1_licenses))
        return h1_licenses_element.is_displayed()
