"""Модуль для тестирования при использовании selenium"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from home_page import HomePage
from search_page import SearchPage


def p(*args) -> None:
    """Функция печати. Строка с пунктуацией. Печатает в консоль."""
    print(*args)


def test() -> None:
    """Открытие домашней страницы и проверка на соответствие."""
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    home_page = HomePage(driver)
    home_page.open()

    assert "MacBook" in driver.page_source, "Строка поиска не найдена"
    time.sleep(5)
    driver.quit()


def test_search_home() -> None:
    """Нажатие на кнопку поиска и проверка на соответствие."""
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    home_page = SearchPage(driver)
    home_page.open()

    home_page.set_search_query("samsung")
    home_page.click_search_button()

    assert "Search - samsung" in driver.page_source, "Samsung не найден"
    time.sleep(5)
    driver.quit()


def test_search_page() -> None:
    """Поиск по критериям."""
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    search_page = SearchPage(driver)
    search_page.open()

    search_page.set_search_criteria("samsung")
    search_page.click_search_criteria_button()

    assert "Samsung SyncMaster 941BW" in driver.page_source, "Samsung не найден"
    time.sleep(5)
    driver.quit()


def main() -> None:
    """Основная функция. Точка входа в программу."""
    test()
    p("Тест окончен")


if __name__ == "__main__":
    main()
