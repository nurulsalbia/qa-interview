"""Central place for test configuration. Values come from env vars / .env."""
import os

from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://qainterview.netlify.app/")
USERNAME = os.getenv("TEST_USERNAME", "musa")
PASSWORD = os.getenv("TEST_PASSWORD")  # no default on purpose: keep secrets out of code
