from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class SearchPage:
    """Класс для работы со страницами поиска через selenium"""

    def __init__(self, driver: WebDriver):
        """Конструктор класса SearchPage"""
        self.driver = driver

    def open(self) -> None:
        """Открыть главную страницу"""
        self.driver.get(
            "https://tutorialsninja.com/demo/index.php?route=product/search"
        )
        self.driver.maximize_window()

    def set_search_query(self, query: str) -> None:
        """Ввести ключевое слово (в шапке сайта)"""
        self.driver.find_element(By.NAME, "search").send_keys(query)

    def click_search_button(self) -> None:
        """Нажать на кнопку поиска"""
        self.driver.find_element(By.CSS_SELECTOR, "button.btn-default").click()

    def set_search_criteria(self, query: str) -> None:
        """Ввести ключевое слово в Search Criteria"""
        self.driver.find_element(
            By.XPATH, "//input[@placeholder='Keywords']"
        ).send_keys(query)

    def click_search_criteria_button(self) -> None:
        """Клик на поиск в Search Criteria"""
        self.driver.find_element(By.ID, "button-search").click()
