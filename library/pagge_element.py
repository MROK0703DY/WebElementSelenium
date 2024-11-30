from typing import Tuple
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class PageElement:
    """Класс для работы с элементами на странице"""

    def __init__(self, driver: WebDriver, locator: Tuple[str, str]):
        """Конструктор класса"""
        self.driver = driver
        self.locator = locator

    def _get_el(self) -> WebElement:
        """Возвращает WebElement по его локатору"""
        return self.driver.find_element(*self.locator)

    def click(self) -> None:
        """Нажимает на элемент"""
        self._get_el().click()

    def send_keys(self, value: str) -> None:
        """Вводит значение в элемент"""
        self._get_el().send_keys(value)
