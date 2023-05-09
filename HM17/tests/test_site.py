import allure
import pytest
from allure_commons.types import AttachmentType

from HM17.utilities.config_reader import get_user_creds, get_invalid_user_creds, get_invalid_user_data_email_creds, \
    get_invalid_user_data_password_creds, get_user_creds_facebook, get_user_creds_google


@pytest.mark.login
@pytest.mark.regression
def test_login(open_login_page):
    login_page = open_login_page
    ucp_subscription = login_page.set_email(get_user_creds()[0]).set_password(get_user_creds()[1]).click_login_button()
    assert ucp_subscription.is_h1_subscription_displayed(), 'H1 not displayed'


@pytest.mark.login
@pytest.mark.regression
def test_login_invalid(open_login_page):
    login_page = open_login_page
    ucp_subscription = login_page.set_email(get_user_creds()[0]).set_password(
        get_user_creds()[1]).click_login_button()
    assert False(), 'H1 not displayed'


@allure.feature('id_1722: Implamaent login page')
@allure.severity(allure.severity_level.CRITICAL)
@allure.description('This test incorrect login')
@allure.epic('Epic_12312')
@allure.title('Test login')
@pytest.mark.login
@pytest.mark.regression
def test_invalid_email_and_password_1(open_login_page):
    login_page = open_login_page
    message_error = login_page.set_email(get_invalid_user_creds()[0]).set_password(get_invalid_user_creds()[1]). \
        click_login_button_error()
    assert message_error.is_error_message_displayed(), 'Error message not displayed'


@allure.feature('id_1722: Implamaent login page1')
@allure.severity(allure.severity_level.CRITICAL)
@allure.description('This test incorrect login1')
@allure.epic('Epic_123121')
@allure.title('Test login1')
@pytest.mark.login
@pytest.mark.regression
def test_invalid_email_and_password_allll(open_login_page):
    login_page = open_login_page
    with allure.step('Open login page'):
        allure.attach(login_page.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    email, password = get_invalid_user_creds()
    with allure.step(f'Set email and password: {email}/{password}'):
        login_page.set_email(email).set_password(password)
    with allure.step('Click login button and verify error message'):
        message_error = login_page.click_login_button_error()
        assert message_error.is_displayed(), 'Error message not displayed'
    with allure.step('Take a screenshot of the error message'):
        allure.attach(login_page.driver.get_screenshot_as_png(), name='Error Screenshot',
                      attachment_type=AttachmentType.PNG)
    assert False, 'Test Failed: Error message not displayed'  # corrected the test result message


@allure.feature('id_1722: Implamaent login page')
@allure.severity(allure.severity_level.CRITICAL)
@allure.description('This test incorrect login')
@allure.epic('Epic_12312')
@allure.title('Test login')
@pytest.mark.login
@pytest.mark.regression
def test_invalid_email_and_password_invalid(open_login_page):
    login_page = open_login_page
    with allure.step('делаем скриншот'):
        allure.attach(login_page.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    message_error = login_page.set_email(get_invalid_user_creds()[0]).set_password(get_invalid_user_creds()[1]). \
        click_login_button_error()
    with allure.step('Take a screenshot of the error message'):
        allure.attach(login_page.driver.get_screenshot_as_png(), name='Error Screenshot',
                      attachment_type=AttachmentType.PNG)
    assert False, 'Error message not displayed'


@pytest.mark.login
@pytest.mark.regression
def test_click_button_login_without_data(open_login_page):
    login_page = open_login_page
    message_error = login_page.click_login_button_error()
    assert message_error.is_error_message_displayed(), 'Error message not displayed'


@pytest.mark.login
@pytest.mark.regression
def test_invalid_email(open_login_page):
    login_page = open_login_page
    message_error = login_page.set_email(get_invalid_user_data_email_creds()[0]). \
        set_password(get_invalid_user_data_email_creds()[1]). \
        click_login_button_error()
    assert message_error.is_error_message_displayed(), 'Error message not displayed'


@pytest.mark.login
@pytest.mark.regression
def test_invalid_email_failed(open_login_page):
    login_page = open_login_page
    message_error = login_page.set_email(get_invalid_user_data_email_creds()[0]). \
        set_password(get_invalid_user_data_email_creds()[1]). \
        click_login_button_error()
    assert message_error.is_error_message_displayed(), 'Error message not displayed'


@pytest.mark.login
@pytest.mark.regression
def test_invalid_password(open_login_page):
    login_page = open_login_page
    message_error = login_page.set_email(get_invalid_user_data_password_creds()[0]). \
        set_password(get_invalid_user_data_password_creds()[1]).click_login_button_error()
    assert message_error.is_error_message_displayed(), 'Error message not displayed'


@pytest.mark.login
@pytest.mark.regression
def test_login_facebook(open_login_page):
    login_page = open_login_page
    ucp_licenses = login_page.click_login_button_facebook(). \
        set_email_facebook(get_user_creds_facebook()[0]).set_password_facebook \
        (get_user_creds_facebook()[1]).click_login_button_facebook_in_fb()
    assert ucp_licenses.is_h1_licenses_displayed(), 'Not login in the acc facebook'


@pytest.mark.login
@pytest.mark.regression
def test_login_google(open_login_page):
    login_page = open_login_page
    ucp_licenses = login_page.click_login_button_google(). \
        set_email_google(get_user_creds_google()[0]). \
        click_login_button_next_google() \
        .set_password_google(get_user_creds_google()[1]) \
        .click_login_button_google_in_google()
    assert ucp_licenses.is_h1_licenses_displayed(), 'Not login in the acc google'


@pytest.mark.login
@pytest.mark.regression
def test_forgot_password(open_login_page):
    login_page = open_login_page
    forgot_pass = login_page.click_forgot_password_button()
    assert forgot_pass.is_forgot_password_dispayed(), 'Not is forgot password page'


@pytest.mark.login
def test_create_account(open_login_page):
    login_page = open_login_page
    create_acc = login_page.click_create_account_button()
    assert create_acc.is_sign_up_displayed(), 'Not in the registration'


@pytest.mark.login
def test_eye_in_password(open_login_page):
    login_page = open_login_page
    show_input_password = login_page.set_password(get_user_creds()[1]).click_yey()
    assert show_input_password.is_show_password(), 'Password dont show'


@pytest.mark.header
def test_multisearch(open_login_page):
    login_page = open_login_page
    open_multisearch = login_page.click_multisearch()
    assert open_multisearch.is_open_multisearch(), 'Multisearch not show'


@pytest.mark.main
def test_is_main_page(open_main_page):
    main_page = open_main_page
    assert main_page.is_h1_main_page_displayed(), 'Not in main page'


@pytest.mark.main
def test_is_2badges_page(open_main_page):
    main_page = open_main_page
    assert main_page.is_2badges_main_page_displayed(), 'Hasnt 2 badges'


@pytest.mark.main
@pytest.mark.regression
def test_open_popup_registration(open_main_page):
    main_page = open_main_page
    popup = main_page.click_free_download_button()
    assert popup.is_popup_register_displayed(), 'Popup registration not open'


@pytest.mark.main
def test_close_popup_registration(open_main_page):
    main_page = open_main_page
    popup_close = main_page.click_free_download_button().click_close_popup_button()
    assert popup_close.is_h1_main_page_displayed(), 'Popup registration not closed'


@pytest.mark.main
@pytest.mark.regression
def test_go_to_pricing(open_main_page):
    main_page = open_main_page
    price = main_page.click_buy_now_button()
    assert price.is_pricing_displayed(), 'Not in pricing page'


@pytest.mark.header
def test_go_to_pricing_header(open_main_page):
    main_page = open_main_page
    price_head = main_page.click_x_in_banner().click_pricing_head_button()
    assert price_head.is_pricing_displayed(), 'Not in pricing page'


@pytest.mark.header
def test_open_dropdown_products(open_main_page):
    main_page = open_main_page
    products_head = main_page.click_button_products()
    assert products_head.is_open_dropdowm_header(), 'Not open dropdown products'


@pytest.mark.header
def test_open_product_spider_in_dropdown_header(open_main_page):
    main_page = open_main_page
    spider_head = main_page.click_button_products().click_in_dropdown_products_spider_head()
    assert spider_head.is_spider_page_displayed(), 'Not open dropdown spider'


@pytest.mark.header
def test_open_product_checker_in_dropdown_header(open_main_page):
    main_page = open_main_page
    checker_head = main_page.click_button_products().click_in_dropdown_products_checker_head()
    assert checker_head.is_checker_page_displayed(), 'Not open dropdown checker'


@pytest.mark.header
def test_open_pop_up_in_header(open_main_page):
    main_page = open_main_page
    popup = main_page.click_free_download_button_in_header()
    assert popup.is_popup_register_displayed(), 'Popup not opened in header'


@pytest.mark.header
def test_open_pop_up_login_in_header(open_main_page):
    main_page = open_main_page
    popup_log = main_page.click_login_in_header()
    assert popup_log.is_popup_login_displayed(), 'Popup login not opened in header'


@pytest.mark.pricing
def test_open_pricing_page(open_pricing_page):
    pricing_page = open_pricing_page
    assert pricing_page.is_pricing_displayed(), 'Pricing page not opened'


@pytest.mark.pricing
def test_open_pricing_checker(open_pricing_page):
    pricing_page = open_pricing_page
    checker_tab = pricing_page.click_checker_tab_button()
    assert checker_tab.is_checker_tab_displayed(), 'Not open checker'


@pytest.mark.pricing
def test_change_to_lifetime_spider(open_pricing_page):
    pricing_page = open_pricing_page
    lifetime_spider = pricing_page.click_lifetime_radiobutton()
    assert lifetime_spider.is_lifetime_displayed(), 'Not in lifetime'

# def test_click_logo_in_header(open_login_page):
#     global main_page_go
#     login_page = open_login_page
#     try:
#         main_page_go = login_page.click_logo_header()     не получилось понять как обойти алерт
#     except UnexpectedAlertPresentException:
#         alert = login_page.driver.switch_to.alert
#         alert.accept()
#     assert main_page_go.is_h1_main_page_displayed(), 'H1 not displayed'
