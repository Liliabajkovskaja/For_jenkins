import requests
from playwright.sync_api import Page

from utils.constants import default_product_id


def test_events_request(page: Page):

    with page.expect_request("**/*logo1*.png", timeout=4) as first:
      page.goto("https://wikipedia.org")
    print(first.value.url)


def print_request_sent(response):
    assert response.status < 400
    # response.request.timing
    print("Request sent: " + str(response.status), response.url)


def test_listener_request(page: Page):

    product_id = default_product_id()

    # page.on("response", print_request_sent)

    # page.goto('https://demo.playwright.dev/todomvc/')

    resp = requests.get('https://demo.playwright.dev/todomvc/')
    pass