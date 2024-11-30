from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from home_page import HomePage
from search_page import SearchPage
from page_element import PageElement


def p(*args) -> None:
    """Функция печати.Строка с пунктуацией.Печатает в консоль."""
    print(*args)


def test_one() -> None:
    """Работа с главной страницей и полем поиска."""
    driver = webdriver.Chrome()

    home_page = HomePage(driver)
    home_page.open()
    home_page.set_search_query("apple")
    home_page.open()

    assert "MacBook" in driver.page_source
    driver.close()
    driver.quit()


def test_search_home() -> None:
    """Переход на другую страницу по запросу."""
    driver = webdriver.Chrome()

    home_page = HomePage(driver)
    home_page.open()
    home_page.set_search_query("samsung")
    home_page.click_search_button()

    assert "Search - samsung" in driver.page_source, "Строка поиска не найдена"
    driver.close()
    driver.quit()


def test_search_page() -> None:
    """Поиск по критериям."""
    driver = webdriver.Chrome()

    search_page = SearchPage(driver)
    search_page.open()
    search_page.set_search_criteria("samsung")
    search_page.click_search_criteria_button()

    assert (
        "Samsung SyncMaster 941BW" in driver.page_source
    ), "Строка поиска\
        не найдена"
    driver.close()
    driver.quit()


def main() -> None:
    """Главная функция.Точка входа в программу."""
    test_one()
    p("Тест окончен")


if __name__ == "__main__":
    main()
