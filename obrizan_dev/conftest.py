"""Pytest configuration."""

import os
import pytest
from typing import Generator
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.fixture(scope="module")
def driver() -> Generator[WebDriver, None, None]:
    """Returns initialized WebDriver instance with a test page opened."""
    drv = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    abs_path = os.path.abspath("test.html")
    drv.get("file://" + abs_path)
    drv.maximize_window()
    drv.implicitly_wait(10)
    yield drv
    drv.quit()
