from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ForgotPassword:
    def __init__(self, driver):
        self.driver = driver
        self.__wait = WebDriverWait(self.driver, 20, 10)

    __h1_forgot_password_page = (
        By.XPATH, "//span[contains(text(),'To reset the password, enter the email you used to')]")

    def is_forgot_password_dispayed(self):
        is_forgot_password_element = self.__wait.until(EC.visibility_of_element_located(self.__h1_forgot_password_page))
        return is_forgot_password_element.is_displayed()
