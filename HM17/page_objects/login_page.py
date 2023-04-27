from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from HM17.page_objects.forgot_password_page import ForgotPassword
from HM17.page_objects.main_page import MainPage
from HM17.page_objects.signup_page import SignUp
from HM17.page_objects.ucp_licences import UcpLicenses
from HM17.page_objects.ucp_subscription import UcpSubscription
from HM17.utilities.web_ui.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__wait = WebDriverWait(self.driver, 10, 5)

    __email_input = (By.XPATH, "//input[@name= 'email']")
    __password_input = (By.XPATH, "//input[@name= 'password']")
    __login_button = (By.XPATH, "//button[@class= 'NS-button NS-button__greenblue reg__next']")
    __error_message = (By.XPATH, "//span[contains(text(),'Invalid email or password entered')]")

    __login_facebook = (By.XPATH, "//span[contains(text(),'Log in with Facebook')]")
    __form_login_facebook = (By.XPATH, "//div[contains(text(),'Log Into Facebook')]")
    __email_input_facebook = (By.XPATH, "//input[@type='text']")
    __password_input_facebook = (By.XPATH, "//input[@type='password']")
    __login_button_facebook = (By.XPATH, "//button[@id='loginbutton']")

    __login_google = (By.XPATH, "//span[contains(text(),'Log in with Google')]")
    __email_input_google = (By.XPATH, "//input[@id='identifierId']")
    __click_button_next_google = (By.XPATH,
                                  "//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b']")

    __password_input_google = (By.XPATH, "//input[@type='password']")
    __login_button_google = (By.XPATH, "//span[contains(text(),'Далі')]")

    __login_password = (By.XPATH, "//div[@id='password']")

    __forgot_password_button = (By.XPATH, "//span[contains(text(),'Forgot password?')]")
    __create_account_button = (By.XPATH, "//span[contains(text(),'Create an Account')]")

    __eye = (By.XPATH, "//i[@class='fa fa-eye-slash']")
    __show_input_password = (By.XPATH, "//input[@type='text']")

    __header_logo = (By.XPATH, "//img[@class='img-header']")
    __multisearch = (By.XPATH, "//li[@id='searchBtn']")


    def is_log_password_google(self):
        is_log_password_google_element = self.__wait.until(EC.visibility_of_element_located(self.__login_password))
        return is_log_password_google_element.is_displayed()

    def set_email(self, email: str):
        self._send_keys(locator=self.__email_input, value=email)
        return self

    def set_password(self, password: str):
        self._send_keys(locator=self.__password_input, value=password)
        return self

    def click_login_button(self):
        self._click(self.__login_button)
        return UcpSubscription(self.driver)

    def login(self, email, password):
        self.set_email(email).set_password(password).click_login_button()
        return UcpSubscription(self.driver)

    def click_login_button_error(self):
        self._click(self.__login_button)
        return LoginPage(self.driver)

    def click_login_button_facebook(self):
        self._click(self.__login_facebook)
        return self

    def set_email_facebook(self, email: str):
        self._send_keys(locator=self.__email_input_facebook, value=email)
        return self

    def set_password_facebook(self, password: str):
        self._send_keys(locator=self.__password_input_facebook, value=password)
        return self

    def click_login_button_facebook_in_fb(self):
        self._click(self.__login_button_facebook)
        return UcpLicenses(self.driver)

    def login_facebook(self, email, password):
        self.set_email_facebook(email).set_password_facebook(password).click_login_button_facebook_in_fb()
        return UcpSubscription(self.driver)

    def click_login_button_google(self):
        self._click(self.__login_google)
        return self

    def set_email_google(self, email: str):
        self._send_keys(locator=self.__email_input_google, value=email)
        return self

    def click_login_button_next_google(self):
        self._click(self.__click_button_next_google)
        return self.is_log_password_google()

    def set_password_google(self, password: str):
        self._send_keys(locator=self.__password_input_google, value=password)
        return self

    def click_login_button_google_in_google(self):
        self._click(self.__login_button_google)
        return UcpLicenses(self.driver)

    def click_forgot_password_button(self):
        self._click(self.__forgot_password_button)
        return ForgotPassword(self.driver)

    def click_create_account_button(self):
        self._click(self.__create_account_button)
        return SignUp(self.driver)

    def click_yey(self):
        self._click(self.__eye)
        return self

    def click_multisearch(self):
        self._click(self.__multisearch)
        return self

