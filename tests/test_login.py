import re

import pytest
from playwright.sync_api import expect


@pytest.mark.smoke
def test_successful_login(login_page, dashboard_page, credentials):
    """A registered user logs in and lands on the dashboard."""
    username, password = credentials

    response = login_page.login(username, password)

    assert response.ok, f"login_post failed with status {response.status}"
    expect(login_page.page).to_have_url(dashboard_page.URL_PATTERN)
    expect(login_page.error_message).to_be_hidden()


@pytest.mark.negative
def test_login_with_wrong_password_shows_error(login_page, dashboard_page, credentials):
    """Bonus: wrong password keeps the user on the login page with an error."""
    username, _ = credentials

    login_page.login(username, "Definitely-wrong-password1!")

    expect(login_page.error_message).to_be_visible()
    expect(login_page.page).not_to_have_url(dashboard_page.URL_PATTERN)
