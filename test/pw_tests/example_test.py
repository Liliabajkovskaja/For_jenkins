import re
from playwright.sync_api import Page, expect


def test_has_title(get_iphone):
    get_iphone.goto("https://playwright.dev/")



    # Expect a title "to contain" a substring.
    expect(get_iphone).to_have_title(re.compile("Playwright"))


# --browser chromium
def test_get_started_link(get_chrome):
    get_chrome.goto("https://playwright.dev/")

    # get list of locators
    els = get_chrome.locator('//a[@href="/docs/intro"]').all()

    # Click the get started link.
    # home_page.get_started_button.click()
    el2 = get_chrome.get_by_role("link", name="Get started")

    el2.click()

    # Expects page to have a heading with the name of Installation.
    expect(get_chrome.get_by_role("heading", name="Installation")).to_be_visible()


import re
from playwright.sync_api import Page, expect


def test_example(get_chrome) -> None:
    get_chrome.goto("https://demo.playwright.dev/todomvc/")
    get_chrome.goto("https://demo.playwright.dev/todomvc/#/")
    get_chrome.get_by_placeholder("What needs to be done?").click()
    get_chrome.get_by_placeholder("What needs to be done?").fill("first element")
    get_chrome.get_by_placeholder("What needs to be done?").press("Enter")
    get_chrome.get_by_placeholder("What needs to be done?").fill("asd")
    get_chrome.get_by_placeholder("What needs to be done?").press("Enter")
    get_chrome.get_by_role("link", name="Active").click()
    get_chrome.get_by_role("link", name="Completed").click()
    get_chrome.get_by_role("link", name="Active").click()
    get_chrome.locator("li").filter(has_text="asd").get_by_label("Toggle Todo").check()
    get_chrome.get_by_role("link", name="Completed").click()
    expect(get_chrome.get_by_test_id("todo-title")).to_contain_text("asd")
