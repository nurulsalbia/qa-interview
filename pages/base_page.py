from urllib.parse import urljoin

from playwright.sync_api import Page

from config.settings import BASE_URL


class BasePage:
    """Shared behaviour for every page object."""

    path = ""

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(urljoin(BASE_URL, self.path))
        return self
