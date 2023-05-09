from contextlib import suppress

import allure
import pytest
import json

from HM17.constants import ROOT_DIR
from HM17.page_objects.login_page import LoginPage
from HM17.page_objects.main_page import MainPage
from HM17.page_objects.pricing_page import Pricing
from HM17.utilities.driver_factory import driver_factory
# from Homework18.task1.HM18.constants import ROOT_DIR
from Homework18.task1.confiquration import Configuration


@pytest.fixture(scope='session', autouse=True)
def env():
    with open(f'{ROOT_DIR}/configuration/config.json', 'r') as file:
        res = file.read()
        config = json.loads(res)
        return Configuration(**config)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture()
def create_browser(env, request):
    driver = driver_factory(int(env.browser_id))
    driver.maximize_window()
    driver.get(env.app_url)

    yield driver
    if request.node.rep_call.failed:
        with suppress(Exception):
            allure.attach(driver.get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)
    driver.quit()


@pytest.fixture()
def open_login_page(create_browser):
    return LoginPage(create_browser)


def pytest_addoption(parser):
    parser.addoption('--browser_id', action='store', default=1, help='Set browser id')
    parser.addoption('--env', action='store', help='Env')


@pytest.fixture()
def create_browser_for_main(env, request):
    driver = driver_factory(int(env.browser_id))
    driver.maximize_window()
    driver.get(env.app_url_main())
    yield driver
    if request.node.rep_call.failed:
        with suppress(Exception):
            allure.attach(driver.get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)
    driver.quit()


@pytest.fixture()
def open_main_page(create_browser_for_main):
    return MainPage(create_browser_for_main)


@pytest.fixture()
def create_browser_for_pricing(env, request):
    driver = driver_factory(int(env.browser_id))
    driver.maximize_window()
    driver.get(env.app_url_pricing())
    yield driver
    if request.node.rep_call.failed:
        with suppress(Exception):
            allure.attach(driver.get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)


@pytest.fixture()
def open_pricing_page(create_browser_for_pricing):
    return Pricing(create_browser_for_pricing)


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "smoke: for smoke tests"
    )
    config.addinivalue_line(
        "markers", "regression: for regression tests"
    )
