import re

from pages.base_page import BasePage


class DashboardPage(BasePage):
    path = "dashboard.html"
    URL_PATTERN = re.compile(r".*/dashboard\.html")
