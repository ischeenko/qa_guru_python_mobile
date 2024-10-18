import allure
import allure_commons
import pytest
import requests
from appium.options.android import UiAutomator2Options
from selene import browser, support
from utils import attach
import pydant



@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = UiAutomator2Options().load_capabilities({
        'platformName': 'android',
        'platformVersion': '9.0',
        'deviceName': 'Google Pixel 3',

        'app': 'bs://sample.app',

        'bstack:options': {
            'projectName': 'First Python project',
            'buildName': 'browserstack-build-1',
            'sessionName': 'BStack first_test',

            'userName': pydant.config.userName,
            'accessKey': pydant.config.accessKey
        }
    })

    browser.config.driver_remote_url = pydant.config.remote_url
    browser.config.driver_options = options
    browser.config.timeout = pydant.config.timeout


    yield

    attach.add_xml_data(browser)
    attach.add_screenshot(browser)

    browser.quit()

