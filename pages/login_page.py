import re

from playwright.sync_api import Page, Response

from pages.base_page import BasePage


class LoginPage(BasePage):
    path = ""

    def __init__(self, page: Page):
        super().__init__(page)
        # VERIFY these with: playwright codegen https://qainterview.netlify.app/
        self.username_input = page.locator("input:not([type='password'])").first
        self.password_input = page.locator("input[type='password']")
        self.login_button = page.get_by_role("button", name=re.compile("login", re.I))
        self.error_message = page.get_by_text("Invalid username or password")
        self.register_link = page.get_by_role("link", name="Create new user")

    def login(self, username: str, password: str) -> Response:
        """Fill the form, submit, and return the login_post API response."""
        self.username_input.fill(username)
        self.password_input.fill(password)
        with self.page.expect_response(
            lambda r: "login_post" in r.url and r.request.method == "POST"
        ) as response_info:
            self.login_button.click()
        return response_info.value
