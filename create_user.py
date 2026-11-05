import argparse
from getpass import getpass
from urllib.parse import urljoin

from playwright.sync_api import sync_playwright

from config.settings import BASE_URL


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a QA Interview user.")
    parser.add_argument(
        "--headed",
        action="store_true",
        help="Show the Chromium browser while creating the user.",
    )
    args = parser.parse_args()

    username = input("New username: ").strip()
    password = getpass("New password: ")
    if not username or not password:
        parser.error("Username and password must not be empty.")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=not args.headed)
        try:
            page = browser.new_page()
            page.goto(urljoin(BASE_URL, "register"))
            page.get_by_label("Username").fill(username)
            page.get_by_label("Password").fill(password)
            submit_button = page.get_by_role("button", name="Create Account")
            if not submit_button.is_enabled():
                print("Registration form is invalid. Check the form requirements:")
                print(page.locator("body").inner_text())
                return 1

            with page.expect_response(
                lambda response: response.request.method == "POST"
            ) as response_info:
                submit_button.click()

            response = response_info.value
            print(f"Registration returned HTTP {response.status}.")
            if response.ok:
                print(f"User '{username}' created successfully.")
            return 0 if response.ok else 1
        finally:
            browser.close()


if __name__ == "__main__":
    raise SystemExit(main())