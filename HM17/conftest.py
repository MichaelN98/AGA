import json

import pytest

from HM17.constants import ROOT_DIR
from HM17.page_objects.login_page import LoginPage
from HM17.page_objects.main_page import MainPage
from HM17.page_objects.pricing_page import Pricing
from HM17.utilities.config_reader import get_application_url, get_browser_id, get_application_url_for_main_page, \
    get_application_url_for_pricing_page
from HM17.utilities.driver_factory import driver_factory
from Homework18.task1.confiquration import Configuration


@pytest.fixture(scope='session', autouse=True)
def env():
    with open(f'{ROOT_DIR}/configuration/config.json', 'r') as file:
        res = file.read()
        config = json.loads(res)
        return Configuration(**config)


@pytest.fixture()
def create_browser():
    driver = driver_factory(get_browser_id())
    driver.maximize_window()
    driver.get(get_application_url())
    yield driver
    driver.quit()


@pytest.fixture()
def open_login_page(create_browser):
    return LoginPage(create_browser)


@pytest.fixture()
def create_browser_for_main():
    driver = driver_factory(get_browser_id())
    driver.maximize_window()
    driver.get(get_application_url_for_main_page())
    yield driver
    driver.quit()


@pytest.fixture()
def open_main_page(create_browser_for_main):
    return MainPage(create_browser_for_main)


@pytest.fixture()
def create_browser_for_pricing():
    driver = driver_factory(get_browser_id())
    driver.maximize_window()
    driver.get(get_application_url_for_pricing_page())
    yield driver
    driver.quit()


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
