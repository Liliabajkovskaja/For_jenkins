from appium.webdriver.common.appiumby import AppiumBy


def test_find_battery(get_android_settings) -> None:
    el = get_android_settings.find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
    el.click()
    el = get_android_settings.find_element(by=AppiumBy.XPATH, value='//*[contains(@resource-id, "usage_summary")]')
    assert el.text == '100 %'


def test_open_browser(get_android_browser) -> None:
    get_android_browser.get('https://appium.io/')


def test_open_application_len_of_elements(get_android_application) -> None:
    els = get_android_application.find_elements(by=AppiumBy.XPATH, value='//*[contains(@resource-id, "list")]/*')
    assert len(els) == 12


def test_open_application(get_android_application) -> None:
    els = get_android_application.find_elements(by=AppiumBy.XPATH, value='//*[contains(@resource-id, "list")]/*')
    assert len(els) == 12


