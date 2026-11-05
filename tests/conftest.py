import pytest

from config.settings import PASSWORD, USERNAME
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage


@pytest.fixture
def credentials():
    if not PASSWORD:
        pytest.fail("TEST_PASSWORD is not set. Copy .env.example to .env and fill it in.")
    return USERNAME, PASSWORD


@pytest.fixture
def login_page(page):
    return LoginPage(page).open()


@pytest.fixture
def dashboard_page(page):
    return DashboardPage(page)
