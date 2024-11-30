from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from obrizan_dev.home_page import HomePage
from obrizan_dev.search_page import SearchPage
import time


def p(*args) -> None:
    """Функция печати.Строка с пунктуацией.Печатает в консоль."""
    print(*args)


def test_two_move() -> None:
    """Открываем главную страницу и проверяем на соответствие.
    Переходим на страницу поиска и проверяем на соответствие."""
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    home_page = HomePage(driver)
    home_page.open()

    assert "MacBook" in driver.page_source, "Строка поиска не найдена"
    time.sleep(3)

    home_page.set_search_query("samsung")
    home_page.click_search_button()

    assert "Search - samsung" in driver.page_source, "Samsung не найден"
    assert "Samsung SyncMaster 941BW" in driver.page_source, "Samsung не найден"
    time.sleep(5)
    driver.quit()

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    search_page = SearchPage(driver)
    search_page.open()

    search_page.set_search_criteria("samsung")
    search_page.click_search_criteria_button()

    assert "Samsung SyncMaster 941BW" in driver.page_source, "Samsung не найден"
    time.sleep(5)
    driver.quit()


def main() -> None:
    """Основная функуия. Точка входа."""
    test_two_move()
    p("Тест окончен")


if __name__ == "__main__":
    main()
