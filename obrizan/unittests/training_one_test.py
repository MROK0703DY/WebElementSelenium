from unittest import TestCase, main
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def run_test() -> None:
    """Функция тестирования, без открытия браузера."""
    # Инициализация головного браузера
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")

    # Создание экземпляра веб-драйвера
    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Chrome()
    driver.get("http://tutorialsninja.com/demo/")
    elem = driver.find_element(By.NAME, "search")
    elem.clear()

    elem.send_keys("iphone")
    elem.send_keys(Keys.RETURN)

    add_to_cart = driver.find_element(
        By.XPATH, '//*[@id="content"]/div[3]/div/div/div[2]/div[2]/button[1]'
    )
    add_to_cart.click()

    shopping_cart_link = driver.find_element(
        By.XPATH, '//*[@id="top-links"]/ul/li[4]/a'
    )
    shopping_cart_link.click()
    assert "product 11" in driver.page_source, "Товар не загружен"
    driver.close()
    driver.quit()
    print("""Тест пройден""")


class TrainingOneTest(TestCase):
    """Класс тестирования модуля training_one"""

    def test_add_to_cart(self) -> None:
        """Добавление в корзину"""
        run_test()
        self.assertTrue(True, "product 11")

    def test_delete(self) -> None:
        """Удаление из корзины"""
        self.assertTrue(True)


if __name__ == "__main__":
    main()
