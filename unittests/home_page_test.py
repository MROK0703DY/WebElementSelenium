from unittest import TestCase, main
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from library.home_page import HomePage
from library.page_element import PageElement


def p(*args) -> None:
    """Функция печати.Строка с пунктуацией.Печатает в консоль."""
    print(*args)


class HomePageTest(TestCase):
    """Класс для тестирования работы модулей home_page."""
    def setUp(self, driver=WebDriver) -> None:
        self.driver = driver
        self.search_button = PageElement(
            self.driver, (By.CSS_SELECTOR, "button.btn-default")
        )
        self.search_field = PageElement(self.driver, (By.NAME, "search"))
        self.shopping_cart = PageElement(self.driver, (By.LINK_TEXT,
                                                       "button.btn-inverse"))
        self.shopping_cart_menu = PageElement(
            self.driver, (By.LINK_TEXT, "button.btn-inverse")
        )

    def test_open(self) -> None:
        """Тест проверяет открытие главной страницы."""
        home_page = HomePage(driver=WebDriver("https://tutorialsninja.com/demo/index.php"))
        home_page.open()
        self.assertEqual(HomePage.__doc__, """Класс для работы со страницами сайта через selenium""")
        self.assertEqual(HomePage.__init__.__doc__, """Конструктор класса""")
        self.assertTrue(True, "Qafox.com")

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    main()
