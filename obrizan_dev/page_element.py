"""Модуль для работы с элементами на странице."""

from typing import Tuple
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class PageElement:
    """
    Упрощенный и подработанный
    класс для работы с элементами на странице,
    возможно его расширение.
    TODO:
    1. Catch StaleElementReferenceException and re-try the search.
    2. Get different non-standard attributes.
    3. Записать типичные ожидания.
    """

    def __init__(self, driver: WebDriver, locator: Tuple[str, str]):
        """Конструктор класса"""
        self.driver = driver
        self.locator = locator

    def _get_el(self) -> WebElement:
        """Возвращает WebElement по его локатору
        Find element by its locator.
        """
        return self.driver.find_element(*self.locator)

    def click(self) -> None:
        """Нажимает на элемент
        Click on the element.
        """
        self._get_el().click()

    def send_keys(self, value: str) -> None:
        """Вводит значение в elements"""
        self._get_el().send_keys(value)

    def get_text(self) -> str:
        """Возвращает текст элемента"""
        return self._get_el().text

    def value(self) -> str | None:
        """Возвращает значение элемента из поля ввода"""
        return self._get_el().get_attribute("value")

    def clear(self) -> None:
        """Очищает поле ввода"""
        self._get_el().clear()
