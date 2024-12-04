"""Модуль для работы с домашней страницей"""

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class HomePage:
    """Класс для работы со страницами сайта через selenium"""

    def __init__(self, driver: WebDriver):
        """Конструктор класса"""
        self.driver = driver

    def open(self) -> None:
        """Открыть главную страницу"""
        self.driver.get("https://tutorialsninja.com/demo/index.php")
        self.driver.maximize_window()

    def set_search_query(self, query: str) -> None:
        """Ввести ключевое слово (в шапке сайта)"""
        self.driver.find_element(By.NAME, "search").send_keys(query)

    def click_search_button(self) -> None:
        """Нажать на кнопку поиска"""
        self.driver.find_element(By.CSS_SELECTOR, "button.btn-default").click()

    def click_shopping_cart_button(self) -> None:
        """Нажать на корзину"""
        self.driver.find_element(By.CSS_SELECTOR, "button.btn-inverse").click()

    def click_shopping_cart_menu(self) -> None:
        """Нажать на меню корзины"""
        self.driver.find_element(By.LINK_TEXT, "Shopping Cart").click()
