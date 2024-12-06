"""Первоначальный туториал по работе со страницами сайта"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from home_page_ob import HomePage
from search_page_ob import SearchPage


def p(*args) -> None:
    """Функция печати. Строка с пунктуацией. Печатает в консоль."""
    print(*args)


def open_home() -> None:
    """Открытие домашней страницы и проверка на соответствие."""
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    home_page = HomePage(driver)
    home_page.open()

    assert "MacBook" in driver.page_source, "Строка поиска не найдена"
    time.sleep(5)
    driver.quit()


def search_home() -> None:
    """Нажатие на кнопку поиска и проверка на соответствие."""
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    home_page = SearchPage(driver)
    home_page.open()

    home_page.set_search_query("samsung")
    home_page.click_search_button()

    assert "Search - samsung" in driver.page_source, "Samsung не найден"
    time.sleep(5)
    driver.quit()


def search_page() -> None:
    """Поиск по критериям."""
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    search_on_page = SearchPage(driver)
    search_on_page.open()

    search_on_page.set_search_criteria("samsung")
    search_on_page.click_search_criteria_button()

    assert "Samsung SyncMaster 941BW" in driver.page_source, "Samsung не найден"
    time.sleep(5)
    driver.quit()


def main() -> None:
    """Основная функция. Точка входа в программу."""
    open_home()
    p("Тест окончен")
    p(27.50)


if __name__ == "__main__":
    main()
