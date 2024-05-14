import pytest
from playwright.sync_api import sync_playwright, Page, Playwright


@pytest.fixture()
def get_chrome() -> Page:

    with sync_playwright() as pw:

        browser = pw.chromium.launch(channel='chrome', headless=False)
        context = browser.new_context(viewport={'width': 1280, 'height': 1024 })
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = context.new_page()

        yield page

        page.close()
        context.tracing.stop(path="trace.zip")
        context.close()
        browser.close()


@pytest.fixture()
def get_iphone(playwright: Playwright) -> Page:

    iphone_13 = playwright.devices['iPhone 13']
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(
        **iphone_13,
    )

    page = context.new_page()

    yield page

    page.close()
    context.close()
    browser.close()
