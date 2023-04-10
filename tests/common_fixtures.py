import os
import pytest
from selenium import webdriver

from lib.config import settings


@pytest.fixture
def selenium(selenium):
    selenium.set_window_size(1500, 1100)
    selenium.implicitly_wait(8)

    return selenium

@pytest.fixture
def chrome_options(chrome_options):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--no-sandbox')

    return chrome_options

@pytest.fixture(scope="session")
def base_url():
    env_var = os.environ.get('BASE_URL')

    url = settings.BASE_URL if env_var is None else env_var

    return url