"""Модуль для тестирования check_one.py."""

import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from obrizan.check_one_ob import open_home, search_home, search_page, p
from obrizan.home_page_ob import HomePage
from obrizan.search_page_ob import SearchPage


@pytest.mark.parametrize(
    "query, expected_result",
    [
        ("samsung", "Samsung SyncMaster 941BW"),
        ("macbook", "MacBook"),
    ],
)

@pytest.fixture(scope="module")
def create_and_open_a_browser():
    """Фикстура для открытия браузера."""
    # Инициализация головного браузера
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")

    # Создание экземпляра веб-драйвера
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options
    )

def test_open_home(create_and_open_a_browser) -> None:
    """Функция тестирования, без открытия браузера."""

    home_page = HomePage(driver)
    home_page.open()

    assert "MacBook" in driver.page_source, "Строка поиска не найдена"
    assert test_open_home.__doc__ == "Функция тестирования, без открытия браузера."
    assert open_home.__doc__ == "Открытие домашней страницы и проверка на соответствие."

    p("  ", test_open_home.__doc__)
    p("\nTest open_home good")


def test_search_home(create_and_open_a_browser) -> None:
    """Функция тестирования нажатия на кнопку, без открытия браузера."""

    home_page = SearchPage(driver)
    home_page.open()

    home_page.set_search_query("samsung")
    home_page.click_search_button()

    assert "Search - samsung" in driver.page_source, "Samsung не найден"
    assert search_home.__doc__ == "Нажатие на кнопку поиска и проверка на соответствие."
    assert (
        test_search_home.__doc__
        == "Функция тестирования нажатия на кнопку, без открытия браузера."
    )

    p("  ", test_search_home.__doc__)
    p("\nTest search_home good")


def test_search_page(create_and_open_a_browser) -> None:
    """Функция тестирования поиска по критериям, без открытия браузера."""

    search_on_page = SearchPage(driver)
    search_on_page.open()

    search_on_page.set_search_criteria("samsung")
    search_on_page.click_search_criteria_button()

    assert "Samsung SyncMaster 941BW" in driver.page_source, "Samsung не найден"
    assert search_page.__doc__ == "Поиск по критериям."
    assert (
        test_search_page.__doc__
        == "Функция тестирования поиска по критериям, без открытия браузера."
    )
    p("  ", test_search_page.__doc__)
    p("\nTest search_page good")
