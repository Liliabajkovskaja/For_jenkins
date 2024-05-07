import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from os.path import join

from utils.config_manager import ConfigManager
from utils.constants import ROOT_PATH

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='com.android.settings',
    appActivity='.Settings',
    language='en',
    locale='US'
)

current_folder = join(join(ROOT_PATH, 'test'), 'mobile_tests')


@pytest.fixture()
def get_android_settings():

    driver = webdriver.Remote(ConfigManager.appium_url, options=UiAutomator2Options().load_capabilities(capabilities))

    driver.implicitly_wait(5)

    yield driver

    driver.quit()


@pytest.fixture()
def get_android_browser():
    _options = UiAutomator2Options()
    _options.platform_name = 'Android'
    _options.automation_name = 'uiautomator2'
    _options.device_name = 'Android_2'
    _options.browser_name = 'chrome'
    _options.chromedriver_executable = join(current_folder, 'chromedriver.exe') # test/mobile_tests/chromedriver.exe

    driver = webdriver.Remote(ConfigManager.appium_url, options=_options)

    driver.implicitly_wait(5)

    yield driver

    driver.quit()


@pytest.fixture()
def get_android_application():
    _options = UiAutomator2Options()
    _options.platform_name = 'Android'
    _options.automation_name = 'uiautomator2'
    _options.device_name = 'Android_3'
    _options.app = join(current_folder, 'ApiDemos-debug.apk')
    # _options.app_package = ''

    driver = webdriver.Remote(ConfigManager.appium_url, options=_options)

    driver.implicitly_wait(5)

    yield driver

    driver.quit()
