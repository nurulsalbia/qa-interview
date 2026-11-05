# QA Interview: UI + API tests

Target: https://qainterview.netlify.app/

## Structure
```
config/settings.py   env-based configuration
pages/               Page Object Model (BasePage, LoginPage, DashboardPage)
tests/               pytest + Playwright tests
postman/             collection + environment (watchlist_post, watchlist_get)
```

## Setup
```bash
python -m venv venv && source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium
cp .env.example .env                              # then set TEST_PASSWORD
```
Register the test user once at https://qainterview.netlify.app/register
(same username/password as in `.env`).

## Run UI tests
```bash
pytest                       # headless
pytest --headed              # watch it run
pytest -m smoke              # only the successful-login test
```

## Create a user
```bash
python create_user.py        # prompts for username and password
python create_user.py --headed
```
The password is entered without being displayed. It must be at least 8 characters
and include uppercase, lowercase, numeric, and special characters.

## Postman
Import both files from `postman/`, select the **QA Interview** environment,
then run the collection (watchlist_post runs first, then watchlist_get).

## Notes / assumptions
- Endpoints are Netlify functions under `/.netlify/functions/`.
- Responses are JSON but sent as `text/plain`, so tests parse the body with `pm.response.json()`.
- The test user must already be registered.
- Re-running `watchlist_post` may add AAPL again for the same user.
