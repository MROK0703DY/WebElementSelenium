from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from home_page import HomePage


def test() -> None:
    """Открытие главной страницы и проверка на соответствие."""
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    home_page = HomePage(driver)
    home_page.open()

    home_page.set_search_query("MacBook")
    home_page.click()

    assert "MacBook" in driver.page_source
    driver.close()
    driver.quit()


def main() -> None:
    """Основная функция.Точка входа в программу."""
    test()


if __name__ == "__main__":
    main()
