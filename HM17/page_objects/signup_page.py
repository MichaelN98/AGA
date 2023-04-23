from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SignUp:
    def __init__(self, driver):
        self.driver = driver
        self.__wait = WebDriverWait(self.driver, 20, 10)

    __h1_sign_up_page = (
        By.XPATH, "//h1[contains(text(),'Great SEO starts with an account')]")

    def is_sign_up_displayed(self):
        is_sign_up_element = self.__wait.until(EC.visibility_of_element_located(self.__h1_sign_up_page))
        return is_sign_up_element.is_displayed()
