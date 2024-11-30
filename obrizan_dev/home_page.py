from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from obrizan_dev.page_element import PageElement


class HomePage:
    """Класс для работы со страницами сайта через selenium"""

    def __init__(self, driver: WebDriver):
        """Конструктор класса"""
        self.driver = driver
        self.search_button = PageElement(
            self.driver, (By.CSS_SELECTOR, "button.btn-default")
        )
        self.search_field = PageElement(self.driver, (By.NAME, "search"))
        self.shopping_cart = PageElement(
            self.driver, (By.CSS_SELECTOR, "button.btn-default")
        )
        self.shopping_cart_menu = PageElement(
            self.driver, (By.LINK_TEXT, "Shopping Cart")
        )

    def open(self) -> None:
        """Открыть главную страницу"""
        self.driver.get("https://tutorialsninja.com/demo/index.php")
        self.driver.maximize_window()

    def set_search_query(self, query: str) -> None:
        """Ввести ключевое слово (в шапке сайта)"""
        self.search_field.send_keys(query)

    def click_search_button(self) -> None:
        """Нажать на кнопку поиска"""
        self.search_button.click()

    def click_shopping_cart_button(self) -> None:
        """Нажать на корзину"""
        self.shopping_cart.click()

    def click_shopping_cart_menu(self) -> None:
        """Нажать на меню корзины"""
        self.shopping_cart_menu.click()
